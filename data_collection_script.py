"""
Data Collection Script for Reddit and YouTube
Based on the Israel-Hamas War Research Paper Methodology

This script sets up configuration files for Reddit and YouTube data collection,
following the methodology described in:
 - "Israel–Hamas war through Telegram, Reddit and Twitter"
 - "Sentiment analysis of the Hamas–Israel war on YouTube comments using deep learning"
"""

import json
import csv
from datetime import datetime
from typing import List, Dict
import os


class SocialMediaDataCollector:
    """
    Collector for social media data from Reddit and YouTube
    """

    def __init__(self, output_dir: str = "collected_data"):
        """
        Initialize the data collector
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    # -------------------------------
    # Reddit Setup
    # -------------------------------
    def setup_reddit_collection(self, subreddits: List[str],
                                keywords: List[str],
                                start_date: str, end_date: str,
                                max_posts: int = 10000):
        """
        Setup Reddit data collection configuration
        """
        print("=" * 60)
        print("REDDIT DATA COLLECTION SETUP")
        print("=" * 60)
        print("\nSubreddits to monitor:")
        for i, subreddit in enumerate(subreddits, 1):
            print(f"{i}. r/{subreddit}")

        print("\nKeywords to search:")
        for i, keyword in enumerate(keywords, 1):
            print(f"{i}. {keyword}")

        print(f"\nDate Range: {start_date} to {end_date}")
        print(f"Max Posts: {max_posts}")
        print("\nRequired Setup:")
        print("1. Install: pip install praw python-dotenv pandas")
        print("2. Get Reddit API credentials from https://www.reddit.com/prefs/apps")
        print("3. Save as environment variables: REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT")

        return self._create_reddit_config(subreddits, keywords, start_date, end_date, max_posts)

    def _create_reddit_config(self, subreddits: List[str], keywords: List[str],
                              start_date: str, end_date: str, max_posts: int) -> Dict:
        """
        Create configuration file for Reddit collection
        """
        config = {
            "platform": "reddit",
            "subreddits": subreddits,
            "keywords": keywords,
            "start_date": start_date,
            "end_date": end_date,
            "max_posts": max_posts,
            "fields_to_collect": [
                "post_id",
                "subreddit",
                "author",
                "date",
                "title",
                "text",
                "score",
                "num_comments",
                "upvote_ratio"
            ]
        }

        config_path = os.path.join(self.output_dir, "reddit_config.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Configuration saved to: {config_path}")
        return config

    # -------------------------------
    # YouTube Setup
    # -------------------------------
    def setup_youtube_collection(self, channels: Dict[str, str],
                                 start_date: str, end_date: str,
                                 max_videos: int = 10,
                                 max_comments: int = 500):
        """
        Setup YouTube data collection configuration
        """
        print("\n" + "=" * 60)
        print("YOUTUBE DATA COLLECTION SETUP")
        print("=" * 60)
        print("\nChannels to monitor:")
        for i, (name, cid) in enumerate(channels.items(), 1):
            print(f"{i}. {name} ({cid})")

        print(f"\nDate Range: {start_date} to {end_date}")
        print(f"Max Videos per Channel: {max_videos}")
        print(f"Max Comments per Video: {max_comments}")
        print("\nRequired Setup:")
        print("1. Install: pip install google-api-python-client python-dotenv pandas")
        print("2. Get YouTube API key from https://console.cloud.google.com/apis/credentials")
        print("3. Save as environment variable: YOUTUBE_API_KEY")

        return self._create_youtube_config(channels, start_date, end_date, max_videos, max_comments)

    def _create_youtube_config(self, channels: Dict[str, str],
                               start_date: str, end_date: str,
                               max_videos: int, max_comments: int) -> Dict:
        """
        Create configuration file for YouTube collection
        """
        config = {
            "platform": "youtube",
            "channels": channels,
            "start_date": start_date,
            "end_date": end_date,
            "max_videos_per_channel": max_videos,
            "max_comments_per_video": max_comments,
            "fields_to_collect": [
                "video_id",
                "comment_id",
                "author",
                "text",
                "published_at",
                "like_count",
                "reply_count",
                "channel_name"
            ]
        }

        config_path = os.path.join(self.output_dir, "youtube_config.json")
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Configuration saved to: {config_path}")
        return config

    # -------------------------------
    # Summary Report
    # -------------------------------
    def create_summary_report(self, reddit_count: int, youtube_count: int):
        """
        Create a summary report of collected data
        """
        report = {
            "collection_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "datasets": {
                "reddit": {"total_posts": reddit_count, "platform": "Reddit"},
                "youtube": {"total_comments": youtube_count, "platform": "YouTube"},
            },
            "total_records": reddit_count + youtube_count
        }

        report_path = os.path.join(self.output_dir, "collection_summary.json")
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print("\n" + "=" * 60)
        print("DATA COLLECTION SUMMARY")
        print("=" * 60)
        print(f"Reddit Posts: {reddit_count:,}")
        print(f"YouTube Comments: {youtube_count:,}")
        print(f"Total Records: {report['total_records']:,}")
        print(f"\n✓ Summary saved to: {report_path}")


def main():
    """
    Main function to setup data collection for Reddit and YouTube
    """
    print("=" * 60)
    print("SOCIAL MEDIA DATA COLLECTION SETUP")
    print("Platforms: Reddit + YouTube")
    print("=" * 60)

    collector = SocialMediaDataCollector()

    # ---------- Reddit ----------
    reddit_subreddits = [
        "Palestine",
        "Israel",
        "IsraelPalestine",
        "worldnews",
        "news",
        "MiddleEastNews",
        "geopolitics"
    ]

    reddit_keywords = [
        "Palestine",
        "Gaza",
        "Israel",
        "Hamas",
        "IDF",
        "West Bank",
        "Gaza Strip",
        "Israeli occupation"
    ]

    reddit_config = collector.setup_reddit_collection(
        subreddits=reddit_subreddits,
        keywords=reddit_keywords,
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_posts=10000
    )

    # ---------- YouTube ----------
    youtube_channels = {
        "BBC": "UC16niRr50-MSBwiO3YDb3RA",
        "Aljazeera": "UCNye-wNBqNL5ZzHSJj3l8Bg",
        "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
        "WION": "UC_gUM8rL-Lrg6O3adPW9K1g",
        "Reuters": "UCZLZ8Jjx_RN2CXloOmgTHVg"
    }

    youtube_config = collector.setup_youtube_collection(
        channels=youtube_channels,
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_videos=10,
        max_comments=500
    )

    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("\nNext Steps:")
    print("1. Review the configuration files in 'collected_data' folder")
    print("2. Add your API credentials to the .env file")
    print("3. Run:")
    print("   - reddit_collector.py for Reddit data")
    print("   - youtube_collector.py for YouTube data")
    print("\nNote: This script sets up the collection framework only.")
    print("Actual collection requires API keys and the implementation files.")


if __name__ == "__main__":
    main()
