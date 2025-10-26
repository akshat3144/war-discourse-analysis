"""
Twitter/X Data Collection Implementation
Collects tweets using snscrape (no API key needed)
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
import json
import os
from typing import List, Dict

class TwitterCollector:
    """
    Collects tweets using snscrape library
    """
    
    def __init__(self, output_dir: str = "collected_data"):
        """
        Initialize Twitter collector
        
        Args:
            output_dir: Directory to save collected data
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def collect_tweets_by_keyword(self, keyword: str, 
                                  start_date: str,
                                  end_date: str,
                                  max_tweets: int = 10000) -> List[Dict]:
        """
        Collect tweets containing a specific keyword
        
        Args:
            keyword: Keyword or hashtag to search
            start_date: Start date in format 'YYYY-MM-DD'
            end_date: End date in format 'YYYY-MM-DD'
            max_tweets: Maximum number of tweets to collect
        
        Returns:
            List of tweet dictionaries
        """
        tweets = []
        
        # Build search query
        query = f"{keyword} since:{start_date} until:{end_date} lang:en"
        
        print(f"\nCollecting tweets for: {keyword}")
        print(f"Query: {query}")
        
        try:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
                if i >= max_tweets:
                    break
                
                tweet_data = {
                    'tweet_id': tweet.id,
                    'date': tweet.date.isoformat(),
                    'username': tweet.user.username,
                    'user_followers': tweet.user.followersCount,
                    'text': tweet.rawContent,
                    'retweet_count': tweet.retweetCount,
                    'like_count': tweet.likeCount,
                    'reply_count': tweet.replyCount,
                    'quote_count': tweet.quoteCount,
                    'language': tweet.lang,
                    'hashtags': tweet.hashtags if hasattr(tweet, 'hashtags') else [],
                    'url': tweet.url,
                    'keyword': keyword
                }
                
                tweets.append(tweet_data)
                
                if (i + 1) % 100 == 0:
                    print(f"  Collected {i + 1} tweets...")
            
            print(f"✓ Collected {len(tweets)} tweets for '{keyword}'")
            
        except Exception as e:
            print(f"✗ Error collecting tweets for '{keyword}': {str(e)}")
        
        return tweets
    
    def collect_tweets_multiple_keywords(self, keywords: List[str],
                                        start_date: str,
                                        end_date: str,
                                        max_tweets_per_keyword: int = 5000) -> List[Dict]:
        """
        Collect tweets for multiple keywords
        
        Args:
            keywords: List of keywords/hashtags
            start_date: Start date in format 'YYYY-MM-DD'
            end_date: End date in format 'YYYY-MM-DD'
            max_tweets_per_keyword: Max tweets per keyword
        
        Returns:
            Combined list of all tweets
        """
        all_tweets = []
        
        for keyword in keywords:
            tweets = self.collect_tweets_by_keyword(
                keyword, start_date, end_date, max_tweets_per_keyword
            )
            all_tweets.extend(tweets)
        
        # Remove duplicates based on tweet_id
        unique_tweets = {tweet['tweet_id']: tweet for tweet in all_tweets}
        all_tweets = list(unique_tweets.values())
        
        print(f"\n✓ Total unique tweets collected: {len(all_tweets)}")
        
        return all_tweets
    
    def save_data(self, tweets: List[Dict], filename: str = None):
        """
        Save collected tweets to JSON and CSV
        
        Args:
            tweets: List of tweet dictionaries
            filename: Base filename (optional)
        """
        if not filename:
            filename = f"twitter_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Save as JSON
        json_path = os.path.join(self.output_dir, f"{filename}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(tweets, f, indent=2, ensure_ascii=False)
        
        # Save as CSV
        csv_path = os.path.join(self.output_dir, f"{filename}.csv")
        df = pd.DataFrame(tweets)
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        print(f"\n✓ Data saved:")
        print(f"  JSON: {json_path}")
        print(f"  CSV: {csv_path}")
        print(f"  Total tweets: {len(tweets)}")
        
        # Create summary
        summary = {
            'total_tweets': len(tweets),
            'date_range': {
                'earliest': min(t['date'] for t in tweets) if tweets else None,
                'latest': max(t['date'] for t in tweets) if tweets else None
            },
            'unique_users': len(set(t['username'] for t in tweets)),
            'collection_date': datetime.now().isoformat()
        }
        
        summary_path = os.path.join(self.output_dir, f"{filename}_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Summary saved to: {summary_path}")


def main():
    """
    Main function to collect Twitter data
    """
    print("=" * 60)
    print("TWITTER DATA COLLECTION")
    print("=" * 60)
    
    # Initialize collector
    collector = TwitterCollector()
    
    # Keywords from paper context
    KEYWORDS = [
        "#FreePalestine",
        "#Gaza",
        "#Israel",
        "#Palestine",
        "#IsraelHamas",
        "#GazaUnderAttack",
        "#PalestineWillBeFree",
        "Gaza conflict",
        "Israel Hamas war",
        "Palestinian solidarity"
    ]
    
    # Date range (from the paper)
    START_DATE = "2023-10-07"
    END_DATE = "2025-01-20"
    
    # Maximum tweets per keyword
    MAX_TWEETS_PER_KEYWORD = 2000
    
    # Collect tweets
    print(f"\nCollecting tweets from {START_DATE} to {END_DATE}")
    tweets = collector.collect_tweets_multiple_keywords(
        KEYWORDS,
        START_DATE,
        END_DATE,
        MAX_TWEETS_PER_KEYWORD
    )
    
    # Save data
    collector.save_data(tweets, filename="twitter_israel_palestine")
    
    print("\n" + "=" * 60)
    print("COLLECTION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    # Note: Install snscrape first: pip install snscrape
    main()
