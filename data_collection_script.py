"""
Data Collection Script for Reddit, YouTube, and Telegram
Based on the Israel–Hamas War Research Methodology

Creates configuration files for Reddit, YouTube, and Telegram
data collection scripts, following the methodology described in:
 - "Israel–Hamas war through Telegram, Reddit and Twitter"
 - "Sentiment analysis of the Hamas–Israel war on YouTube comments using deep learning"
"""

import json
from datetime import datetime
from typing import List, Dict
import os


class SocialMediaDataCollector:
    """
    Config setup for social media data collection
    """

    def __init__(self, output_dir: str = "collected_data"):
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
        for i, s in enumerate(subreddits, 1):
            print(f"{i}. r/{s}")

        print("\nKeywords:")
        for i, k in enumerate(keywords, 1):
            print(f"{i}. {k}")

        print(f"\nDate Range: {start_date} → {end_date}")
        print(f"Max Posts: {max_posts}")

        config = {
            "platform": "reddit",
            "subreddits": subreddits,
            "keywords": keywords,
            "start_date": start_date,
            "end_date": end_date,
            "max_posts": max_posts,
            "fields_to_collect": [
                "post_id", "subreddit", "author", "date", "title",
                "text", "score", "num_comments", "upvote_ratio"
            ]
        }

        path = os.path.join(self.output_dir, "reddit_config.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Reddit configuration saved → {path}")
        return config

    # -------------------------------
    # YouTube Setup
    # -------------------------------
    def setup_youtube_collection(self, channels: Dict[str, str],
                                 start_date: str, end_date: str,
                                 max_videos: int = 10,
                                 max_comments: int = 500,
                                 keywords: List[str] = None):
        """
        Setup YouTube data collection configuration
        """
        print("\n" + "=" * 60)
        print("YOUTUBE DATA COLLECTION SETUP")
        print("=" * 60)

        print("\nChannels to monitor:")
        for i, (name, cid) in enumerate(channels.items(), 1):
            print(f"{i}. {name} ({cid})")

        print("\nKeywords:")
        if keywords:
            for i, k in enumerate(keywords, 1):
                print(f"{i}. {k}")

        print(f"\nDate Range: {start_date} → {end_date}")
        print(f"Max Videos per Channel: {max_videos}")
        print(f"Max Comments per Video: {max_comments}")

        config = {
            "platform": "youtube",
            "channels": channels,
            "keywords": keywords or [],
            "start_date": start_date,
            "end_date": end_date,
            "max_videos_per_channel": max_videos,
            "max_comments_per_video": max_comments,
            "fields_to_collect": [
                "video_id", "comment_id", "author", "text",
                "published_at", "like_count", "reply_count", "channel_name"
            ]
        }

        path = os.path.join(self.output_dir, "youtube_config.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ YouTube configuration saved → {path}")
        return config

    # -------------------------------
    # Telegram Setup
    # -------------------------------
    def setup_telegram_collection(self, channels: List[str],
                                  start_date: str, end_date: str,
                                  max_messages: int = 2000):
        """
        Setup Telegram data collection configuration
        """
        print("\n" + "=" * 60)
        print("TELEGRAM DATA COLLECTION SETUP")
        print("=" * 60)

        print("\nChannels to monitor:")
        for i, ch in enumerate(channels, 1):
            print(f"{i}. {ch}")

        print(f"\nDate Range: {start_date} → {end_date}")
        print(f"Max Messages per Channel: {max_messages}")
        print("\nRequired Setup:")
        print("1. Install: pip install telethon python-dotenv pandas")
        print("2. Create .env file with TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE")

        config = {
            "platform": "telegram",
            "channels": channels,
            "start_date": start_date,
            "end_date": end_date,
            "max_messages_per_channel": max_messages,
            "fields_to_collect": [
                "channel_name", "message_id", "date", "text",
                "views", "forwards", "replies", "media"
            ]
        }

        path = os.path.join(self.output_dir, "telegram_config.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Telegram configuration saved → {path}")
        return config

    # -------------------------------
    # Summary Report
    # -------------------------------
    def create_summary_report(self, reddit_count: int, youtube_count: int, telegram_count: int):
        """
        Create summary report for all three platforms
        """
        report = {
            "collection_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "datasets": {
                "reddit": {"total_posts": reddit_count, "platform": "Reddit"},
                "youtube": {"total_comments": youtube_count, "platform": "YouTube"},
                "telegram": {"total_messages": telegram_count, "platform": "Telegram"}
            },
            "total_records": reddit_count + youtube_count + telegram_count
        }

        path = os.path.join(self.output_dir, "collection_summary.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print("\n" + "=" * 60)
        print("DATA COLLECTION SUMMARY")
        print("=" * 60)
        print(f"Reddit Posts: {reddit_count:,}")
        print(f"YouTube Comments: {youtube_count:,}")
        print(f"Telegram Messages: {telegram_count:,}")
        print(f"Total Records: {report['total_records']:,}")
        print(f"\n✓ Summary saved → {path}")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print("=" * 60)
    print("SOCIAL MEDIA DATA COLLECTION SETUP")
    print("Platforms: Reddit + YouTube + Telegram")
    print("=" * 60)

    collector = SocialMediaDataCollector()

    # ---------- Reddit ----------
    reddit_config = collector.setup_reddit_collection(
        subreddits=[
            "Palestine", "Israel", "IsraelPalestine", "worldnews",
            "news", "MiddleEastNews", "geopolitics"
        ],
        keywords=[
            "Palestine", "Gaza", "Israel", "Hamas",
            "IDF", "West Bank", "Gaza Strip", "Israeli occupation"
        ],
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_posts=10000
    )

    # ---------- YouTube ----------
    youtube_config = collector.setup_youtube_collection(
        channels={
            "BBC": "UC16niRr50-MSBwiO3YDb3RA",
            "Aljazeera": "UCNye-wNBqNL5ZzHSJj3l8Bg",
            "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
            "WION": "UC_gUM8rL-Lrg6O3adPW9K1g",
            "Reuters": "UCZLZ8Jjx_RN2CXloOmgTHVg"
        },
        keywords=["Israel", "Hamas", "Gaza", "Palestine", "conflict", "war"],
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_videos=10,
        max_comments=500
    )

    # ---------- Telegram ----------
    telegram_channels = [
        "AlQassamBrigades", "Aqsatvsat", "Eyeonpalestine", "FreePalestine2023",
        "GazaNow", "PalestineSolidarityBelgium", "PalestineUpdates",
        "PalestinianResistance", "StopGazaGenocide", "TIMESOFGAZA",
        "TheJerusalemPost", "bigolivr", "gazaalanpa", "gazaenglishupdates",
        "haqqintel", "palOnline", "palestineonline", "palestineresistance", "resistancechain"
    ]

    telegram_config = collector.setup_telegram_collection(
        channels=telegram_channels,
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_messages=2000
    )

    print("\n" + "=" * 60)
    print("SETUP COMPLETE ✅")
    print("=" * 60)
    print("\nNext Steps:")
    print("1. Review generated configs in 'collected_data/'")
    print("2. Ensure API credentials in .env file")
    print("3. Run respective collectors:")
    print("   - reddit_collector.py")
    print("   - youtube_collector.py")
    print("   - telegram_collector.py")


if __name__ == "__main__":
    main()
