"""
Reddit Data Collection Implementation
Collects posts and comments from Reddit using PRAW
"""

import praw
from datetime import datetime
import json
import pandas as pd
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Configuration (REPLACE WITH YOUR CREDENTIALS)
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

class RedditCollector:
    """
    Collects data from Reddit using PRAW
    """
    
    def __init__(self, client_id: str, client_secret: str, user_agent: str,
                 output_dir: str = "collected_data"):
        """
        Initialize Reddit collector
        
        Args:
            client_id: Reddit API client ID
            client_secret: Reddit API client secret
            user_agent: User agent string
            output_dir: Directory to save collected data
        """
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        print("✓ Connected to Reddit API")
    
    def collect_subreddit_posts(self, subreddit_name: str,
                               start_date: datetime,
                               end_date: datetime,
                               keywords: List[str] = None,
                               max_posts: int = 10000) -> List[Dict]:
        """
        Collect posts from a subreddit
        
        Args:
            subreddit_name: Name of subreddit (without r/)
            start_date: Start date for collection
            end_date: End date for collection
            keywords: Optional list of keywords to filter
            max_posts: Maximum number of posts to collect
        
        Returns:
            List of post dictionaries
        """
        posts = []
        subreddit = self.reddit.subreddit(subreddit_name)
        
        print(f"\nCollecting from r/{subreddit_name}...")
        
        try:
            # Collect posts
            for post in subreddit.new(limit=max_posts):
                # Check date range
                post_date = datetime.fromtimestamp(post.created_utc)
                
                if post_date < start_date or post_date > end_date:
                    continue
                
                # Filter by keywords if provided
                if keywords:
                    text_to_search = (post.title + " " + post.selftext).lower()
                    if not any(keyword.lower() in text_to_search for keyword in keywords):
                        continue
                
                # Extract post data
                post_data = {
                    'post_id': post.id,
                    'subreddit': subreddit_name,
                    'author': str(post.author) if post.author else '[deleted]',
                    'date': datetime.fromtimestamp(post.created_utc).isoformat(),
                    'title': post.title,
                    'text': post.selftext,
                    'score': post.score,
                    'upvote_ratio': post.upvote_ratio,
                    'num_comments': post.num_comments,
                    'url': post.url,
                    'permalink': f"https://reddit.com{post.permalink}",
                    'is_self': post.is_self
                }
                
                posts.append(post_data)
                
                if len(posts) % 100 == 0:
                    print(f"  Collected {len(posts)} posts...")
            
            print(f"✓ Collected {len(posts)} posts from r/{subreddit_name}")
            
        except Exception as e:
            print(f"✗ Error collecting from r/{subreddit_name}: {str(e)}")
        
        return posts
    
    def collect_post_comments(self, post_id: str, max_comments: int = 100) -> List[Dict]:
        """
        Collect comments from a specific post
        
        Args:
            post_id: Reddit post ID
            max_comments: Maximum number of comments to collect
        
        Returns:
            List of comment dictionaries
        """
        comments = []
        
        try:
            submission = self.reddit.submission(id=post_id)
            submission.comments.replace_more(limit=0)  # Remove "load more" comments
            
            for comment in submission.comments.list()[:max_comments]:
                comment_data = {
                    'comment_id': comment.id,
                    'post_id': post_id,
                    'author': str(comment.author) if comment.author else '[deleted]',
                    'date': datetime.fromtimestamp(comment.created_utc).isoformat(),
                    'text': comment.body,
                    'score': comment.score,
                    'is_submitter': comment.is_submitter,
                    'parent_id': comment.parent_id
                }
                comments.append(comment_data)
        
        except Exception as e:
            print(f"✗ Error collecting comments for post {post_id}: {str(e)}")
        
        return comments
    
    def search_reddit(self, query: str,
                     start_date: datetime,
                     end_date: datetime,
                     subreddits: List[str] = None,
                     max_results: int = 10000) -> List[Dict]:
        """
        Search Reddit for posts matching a query
        
        Args:
            query: Search query
            start_date: Start date for collection
            end_date: End date for collection
            subreddits: Optional list of subreddits to search
            max_results: Maximum number of results
        
        Returns:
            List of post dictionaries
        """
        posts = []
        
        # Search across specified subreddits or all of Reddit
        if subreddits:
            search_target = self.reddit.subreddit('+'.join(subreddits))
        else:
            search_target = self.reddit.subreddit('all')
        
        print(f"\nSearching for: {query}")
        
        try:
            for post in search_target.search(query, limit=max_results, sort='new'):
                post_date = datetime.fromtimestamp(post.created_utc)
                
                if post_date < start_date or post_date > end_date:
                    continue
                
                post_data = {
                    'post_id': post.id,
                    'subreddit': post.subreddit.display_name,
                    'author': str(post.author) if post.author else '[deleted]',
                    'date': post_date.isoformat(),
                    'title': post.title,
                    'text': post.selftext,
                    'score': post.score,
                    'upvote_ratio': post.upvote_ratio,
                    'num_comments': post.num_comments,
                    'url': post.url,
                    'permalink': f"https://reddit.com{post.permalink}",
                    'search_query': query
                }
                
                posts.append(post_data)
                
                if len(posts) % 100 == 0:
                    print(f"  Found {len(posts)} posts...")
            
            print(f"✓ Found {len(posts)} posts for query: {query}")
            
        except Exception as e:
            print(f"✗ Error searching for '{query}': {str(e)}")
        
        return posts
    
    def collect_from_multiple_subreddits(self, subreddits: List[str],
                                        start_date: datetime,
                                        end_date: datetime,
                                        keywords: List[str] = None,
                                        max_posts_per_sub: int = 5000) -> List[Dict]:
        """
        Collect posts from multiple subreddits
        
        Args:
            subreddits: List of subreddit names
            start_date: Start date for collection
            end_date: End date for collection
            keywords: Optional keywords to filter
            max_posts_per_sub: Max posts per subreddit
        
        Returns:
            Combined list of all posts
        """
        all_posts = []
        
        for subreddit in subreddits:
            posts = self.collect_subreddit_posts(
                subreddit, start_date, end_date, keywords, max_posts_per_sub
            )
            all_posts.extend(posts)
        
        # Remove duplicates
        unique_posts = {post['post_id']: post for post in all_posts}
        all_posts = list(unique_posts.values())
        
        print(f"\n✓ Total unique posts collected: {len(all_posts)}")
        
        return all_posts
    
    def save_data(self, posts: List[Dict], filename: str = None):
        """
        Save collected posts to JSON and CSV
        
        Args:
            posts: List of post dictionaries
            filename: Base filename (optional)
        """
        if not filename:
            filename = f"reddit_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Save as JSON
        json_path = os.path.join(self.output_dir, f"{filename}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        
        # Save as CSV
        csv_path = os.path.join(self.output_dir, f"{filename}.csv")
        df = pd.DataFrame(posts)
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        print(f"\n✓ Data saved:")
        print(f"  JSON: {json_path}")
        print(f"  CSV: {csv_path}")
        print(f"  Total posts: {len(posts)}")
        
        # Create summary
        summary = {
            'total_posts': len(posts),
            'date_range': {
                'earliest': min(p['date'] for p in posts) if posts else None,
                'latest': max(p['date'] for p in posts) if posts else None
            },
            'unique_subreddits': len(set(p['subreddit'] for p in posts)),
            'unique_authors': len(set(p['author'] for p in posts)),
            'collection_date': datetime.now().isoformat()
        }
        
        summary_path = os.path.join(self.output_dir, f"{filename}_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Summary saved to: {summary_path}")


def main():
    """
    Main function to collect Reddit data
    """
    print("=" * 60)
    print("REDDIT DATA COLLECTION")
    print("=" * 60)
    
    # Initialize collector
    collector = RedditCollector(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
    
    # Subreddits to collect from
    SUBREDDITS = [
        "Palestine",
        "Israel",
        "IsraelPalestine",
        "worldnews",
        "news",
        "MiddleEastNews",
        "geopolitics"
    ]
    
    # Keywords to search for
    KEYWORDS = [
        "Palestine",
        "Gaza",
        "Israel",
        "Hamas",
        "IDF",
        "West Bank",
        "Gaza Strip",
        "Israeli occupation"
        ]
    
    # Date range (from the paper)
    START_DATE = datetime(2023, 10, 7)
    END_DATE = datetime(2025, 1, 20)
    
    # Collect posts
    print(f"\nCollecting posts from {START_DATE.date()} to {END_DATE.date()}")
    posts = collector.collect_from_multiple_subreddits(
        SUBREDDITS,
        START_DATE,
        END_DATE,
        KEYWORDS,
        max_posts_per_sub=5000
    )
    
    # Save data
    collector.save_data(posts, filename="reddit_israel_palestine")
    
    print("\n" + "=" * 60)
    print("COLLECTION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    # Note: Install PRAW first: pip install praw
    main()
