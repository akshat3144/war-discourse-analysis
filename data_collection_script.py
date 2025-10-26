"""
Data Collection Script for Social Media Analysis
Based on the Israel-Hamas War Research Paper Methodology

This script collects data from Telegram, Twitter (X), and Reddit
following the methodology described in the paper.
"""

import json
import csv
from datetime import datetime
from typing import List, Dict
import os

class SocialMediaDataCollector:
    """
    Collector for social media data from Telegram, Twitter, and Reddit
    """
    
    def __init__(self, output_dir: str = "collected_data"):
        """
        Initialize the data collector
        
        Args:
            output_dir: Directory to save collected data
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def setup_telegram_collection(self, channels: List[str], 
                                  start_date: str, end_date: str):
        """
        Setup Telegram data collection
        
        Args:
            channels: List of Telegram channel usernames
            start_date: Start date in format 'YYYY-MM-DD'
            end_date: End date in format 'YYYY-MM-DD'
        
        Note: Requires Telethon library and Telegram API credentials
        """
        print("=" * 60)
        print("TELEGRAM DATA COLLECTION SETUP")
        print("=" * 60)
        print("\nChannels to monitor:")
        for i, channel in enumerate(channels, 1):
            print(f"{i}. @{channel}")
        print(f"\nDate Range: {start_date} to {end_date}")
        print("\nRequired Setup:")
        print("1. Install: pip install telethon")
        print("2. Get Telegram API credentials from https://my.telegram.org")
        print("3. Save credentials as: api_id and api_hash")
        
        return self._create_telegram_config(channels, start_date, end_date)
    
    def _create_telegram_config(self, channels: List[str], 
                                start_date: str, end_date: str) -> Dict:
        """Create configuration for Telegram collection"""
        config = {
            "platform": "telegram",
            "channels": channels,
            "start_date": start_date,
            "end_date": end_date,
            "fields_to_collect": [
                "message_id",
                "channel_name",
                "date",
                "text",
                "views",
                "forwards",
                "replies",
                "media_type"
            ]
        }
        
        # Save config
        config_path = os.path.join(self.output_dir, "telegram_config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n✓ Configuration saved to: {config_path}")
        return config
    
    def setup_twitter_collection(self, keywords: List[str], 
                                 start_date: str, end_date: str,
                                 max_tweets: int = 10000):
        """
        Setup Twitter/X data collection
        
        Args:
            keywords: List of keywords/hashtags to search
            start_date: Start date in format 'YYYY-MM-DD'
            end_date: End date in format 'YYYY-MM-DD'
            max_tweets: Maximum number of tweets to collect
        
        Note: Requires Twitter API access or snscrape library
        """
        print("\n" + "=" * 60)
        print("TWITTER/X DATA COLLECTION SETUP")
        print("=" * 60)
        print("\nKeywords/Hashtags to monitor:")
        for i, keyword in enumerate(keywords, 1):
            print(f"{i}. {keyword}")
        print(f"\nDate Range: {start_date} to {end_date}")
        print(f"Max Tweets: {max_tweets}")
        print("\nRequired Setup:")
        print("Option 1: Twitter API (Recommended for real-time)")
        print("  - Apply at https://developer.twitter.com")
        print("  - Install: pip install tweepy")
        print("\nOption 2: SNScrape (For historical data)")
        print("  - Install: pip install snscrape")
        
        return self._create_twitter_config(keywords, start_date, end_date, max_tweets)
    
    def _create_twitter_config(self, keywords: List[str], 
                               start_date: str, end_date: str,
                               max_tweets: int) -> Dict:
        """Create configuration for Twitter collection"""
        config = {
            "platform": "twitter",
            "keywords": keywords,
            "start_date": start_date,
            "end_date": end_date,
            "max_tweets": max_tweets,
            "fields_to_collect": [
                "tweet_id",
                "username",
                "date",
                "text",
                "retweet_count",
                "like_count",
                "reply_count",
                "language",
                "hashtags"
            ]
        }
        
        config_path = os.path.join(self.output_dir, "twitter_config.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n✓ Configuration saved to: {config_path}")
        return config
    
    def setup_reddit_collection(self, subreddits: List[str], 
                               keywords: List[str],
                               start_date: str, end_date: str,
                               max_posts: int = 10000):
        """
        Setup Reddit data collection
        
        Args:
            subreddits: List of subreddit names (without r/)
            keywords: List of keywords to search
            start_date: Start date in format 'YYYY-MM-DD'
            end_date: End date in format 'YYYY-MM-DD'
            max_posts: Maximum number of posts to collect
        
        Note: Requires PRAW library and Reddit API credentials
        """
        print("\n" + "=" * 60)
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
        print("1. Install: pip install praw")
        print("2. Get Reddit API credentials from https://www.reddit.com/prefs/apps")
        print("3. Save as: client_id, client_secret, user_agent")
        
        return self._create_reddit_config(subreddits, keywords, start_date, 
                                         end_date, max_posts)
    
    def _create_reddit_config(self, subreddits: List[str], keywords: List[str],
                             start_date: str, end_date: str, max_posts: int) -> Dict:
        """Create configuration for Reddit collection"""
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
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n✓ Configuration saved to: {config_path}")
        return config
    
    def save_data(self, data: List[Dict], platform: str, filename: str = None):
        """
        Save collected data to JSON and CSV formats
        
        Args:
            data: List of collected messages/posts
            platform: Platform name (telegram, twitter, reddit)
            filename: Custom filename (optional)
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{platform}_data_{timestamp}"
        
        # Save as JSON
        json_path = os.path.join(self.output_dir, f"{filename}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Save as CSV
        if data:
            csv_path = os.path.join(self.output_dir, f"{filename}.csv")
            keys = data[0].keys()
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
        
        print(f"\n✓ Data saved:")
        print(f"  JSON: {json_path}")
        print(f"  CSV: {csv_path}")
        print(f"  Total records: {len(data)}")
    
    def create_summary_report(self, telegram_count: int, twitter_count: int, 
                            reddit_count: int):
        """
        Create a summary report of collected data
        
        Args:
            telegram_count: Number of Telegram messages
            twitter_count: Number of tweets
            reddit_count: Number of Reddit posts
        """
        report = {
            "collection_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "datasets": {
                "telegram": {
                    "total_messages": telegram_count,
                    "platform": "Telegram"
                },
                "twitter": {
                    "total_tweets": twitter_count,
                    "platform": "Twitter/X"
                },
                "reddit": {
                    "total_posts": reddit_count,
                    "platform": "Reddit"
                }
            },
            "total_records": telegram_count + twitter_count + reddit_count
        }
        
        report_path = os.path.join(self.output_dir, "collection_summary.json")
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print("\n" + "=" * 60)
        print("DATA COLLECTION SUMMARY")
        print("=" * 60)
        print(f"Telegram Messages: {telegram_count:,}")
        print(f"Twitter Tweets: {twitter_count:,}")
        print(f"Reddit Posts: {reddit_count:,}")
        print(f"Total Records: {report['total_records']:,}")
        print(f"\n✓ Summary saved to: {report_path}")


def main():
    """
    Main function to setup data collection based on paper methodology
    """
    print("=" * 60)
    print("SOCIAL MEDIA DATA COLLECTION SETUP")
    print("Based on Israel-Hamas War Research Paper")
    print("=" * 60)
    
    # Initialize collector
    collector = SocialMediaDataCollector()
    
    # Telegram channels from the paper (Table 1)
    telegram_channels = [
        "AlQassamBrigades",
        "Aqsatvsat",
        "Eyeonpalestine",
        "FreePalestine2023",
        "GazaNow",
        "PalestineSolidarityBelgium",
        "PalestineUpdates",
        "PalestinianResistance",
        "StopGazaGenocide",
        "TIMESOFGAZA",
        "TheJerusalemPost",
        "bigolivr",
        "gazaalanpa",
        "gazaenglishupdates",
        "haqqintel",
        "palOnline",
        "palestineonline",
        "palestineresistance",
        "resistancechain"
    ]
    
    # Setup Telegram collection
    telegram_config = collector.setup_telegram_collection(
        channels=telegram_channels,
        start_date="2023-10-23",
        end_date="2025-01-20"
    )
    
    # Twitter keywords (inferred from paper context)
    twitter_keywords = [
        "#FreePalestine",
        "#Gaza",
        "#Israel",
        "#Palestine",
        "#IsraelHamas",
        "Israel Hamas war",
        "Gaza conflict"
    ]
    
    # Setup Twitter collection
    twitter_config = collector.setup_twitter_collection(
        keywords=twitter_keywords,
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_tweets=10000
    )
    
    # Reddit subreddits (inferred from paper context)
    reddit_subreddits = [
        "Palestine",
        "Israel",
        "IsraelPalestine",
        "worldnews",
        "news"
    ]
    
    # Setup Reddit collection
    reddit_config = collector.setup_reddit_collection(
        subreddits=reddit_subreddits,
        keywords=["Palestine", "Gaza", "Israel", "Hamas"],
        start_date="2023-10-07",
        end_date="2025-01-20",
        max_posts=10000
    )
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("\nNext Steps:")
    print("1. Review the configuration files in 'collected_data' folder")
    print("2. Install required libraries for each platform")
    print("3. Obtain API credentials")
    print("4. Run the actual collection scripts (see implementation files)")
    print("\nNote: This script sets up the collection framework.")
    print("Actual data collection requires API access and additional code.")


if __name__ == "__main__":
    main()
