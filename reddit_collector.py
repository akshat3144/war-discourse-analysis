"""
Reddit Data Collection via Reddit's Public JSON Endpoints
(No API credentials required, reliable alternative to Pushshift)
"""

import requests
import time
from datetime import datetime
import json
import pandas as pd
import os
from typing import List, Dict


class RedditCollector:
    """
    Collects Reddit posts using Reddit's public JSON search endpoints
    """

    def __init__(self, output_dir: str = "collected_data"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.base_url = "https://www.reddit.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (Reddit Data Collector)"}
        print("✓ Connected to Reddit public JSON endpoints")

    def collect_posts(self,
                      subreddits: List[str],
                      keywords: List[str],
                      max_posts_per_sub: int = 500) -> List[Dict]:
        """
        Collect posts from multiple subreddits
        using Reddit's JSON endpoints (no API keys required)
        """
        all_posts = []

        for subreddit in subreddits:
            print(f"\nCollecting from r/{subreddit}...")
            collected = 0

            for keyword in keywords:
                after = None
                while collected < max_posts_per_sub:
                    url = f"{self.base_url}/r/{subreddit}/search.json"
                    params = {
                        "q": keyword,
                        "restrict_sr": "on",
                        "sort": "new",
                        "limit": "100",
                        "after": after
                    }

                    try:
                        response = requests.get(url, headers=self.headers, params=params, timeout=30)
                        if response.status_code != 200:
                            print(f"⚠️ HTTP {response.status_code} for {subreddit} - {keyword}")
                            break

                        data = response.json().get("data", {})
                        posts = data.get("children", [])
                        if not posts:
                            break

                        for post in posts:
                            post_data = post["data"]
                            post_record = {
                                "post_id": post_data.get("id"),
                                "subreddit": subreddit,
                                "author": post_data.get("author"),
                                "date": datetime.utcfromtimestamp(post_data.get("created_utc")).isoformat(),
                                "title": post_data.get("title", ""),
                                "text": post_data.get("selftext", ""),
                                "score": post_data.get("score", 0),
                                "num_comments": post_data.get("num_comments", 0),
                                "upvote_ratio": post_data.get("upvote_ratio"),
                                "url": f"https://reddit.com{post_data.get('permalink', '')}",
                                "keyword": keyword
                            }
                            all_posts.append(post_record)

                        collected += len(posts)
                        print(f"  {keyword}: Collected {collected} posts so far...")
                        after = data.get("after")

                        if not after:
                            break

                        time.sleep(1)  # Avoid hitting rate limits

                    except Exception as e:
                        print(f"✗ Error collecting {subreddit}/{keyword}: {e}")
                        time.sleep(5)
                        break

            print(f"✓ Finished r/{subreddit} — total {collected} posts")

        # Deduplicate by post_id
        unique_posts = {p["post_id"]: p for p in all_posts}
        all_posts = list(unique_posts.values())

        print(f"\n✓ Total unique posts collected: {len(all_posts)}")
        return all_posts

    def save_data(self, posts: List[Dict], filename: str = None):
        """
        Save collected posts to JSON and CSV
        """
        if not filename:
            filename = f"reddit_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        json_path = os.path.join(self.output_dir, f"{filename}.json")
        csv_path = os.path.join(self.output_dir, f"{filename}.csv")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)

        pd.DataFrame(posts).to_csv(csv_path, index=False, encoding="utf-8")

        print(f"\n✓ Data saved:")
        print(f"  JSON → {json_path}")
        print(f"  CSV  → {csv_path}")
        print(f"  Total posts: {len(posts)}")


def main():
    """
    Main execution
    """
    print("=" * 60)
    print("REDDIT DATA COLLECTION (Reliable Public JSON)")
    print("=" * 60)

    collector = RedditCollector()

    SUBREDDITS = [
        "Palestine",
        "Israel",
        "IsraelPalestine",
        "worldnews",
        "news",
        "MiddleEastNews",
        "geopolitics"
    ]

    KEYWORDS = [
        "Palestine", "Gaza", "Israel", "Hamas",
        "IDF", "West Bank", "Gaza Strip", "Israeli occupation"
    ]

    posts = collector.collect_posts(SUBREDDITS, KEYWORDS, max_posts_per_sub=1000)
    collector.save_data(posts, filename="reddit_israel_palestine")

    print("\n" + "=" * 60)
    print("COLLECTION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
