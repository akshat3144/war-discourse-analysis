"""
YouTube Data Collection Implementation
Collects video comments and metadata using YouTube Data API v3
Replicates the methodology from 'Sentiment analysis of the Hamas-Israel war on YouTube comments using deep learning'
"""

import os
import json
import pandas as pd
from datetime import datetime
from typing import List, Dict
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)


class YouTubeCollector:
    """
    Collects data (comments + metadata) from YouTube channels or videos
    """

    def __init__(self, api_key: str, output_dir: str = "collected_data"):
        self.api_key = api_key
        self.youtube = build("youtube", "v3", developerKey=api_key)
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        print("✓ Connected to YouTube Data API")

    def get_channel_videos(self, channel_id: str, max_results: int = 50) -> List[str]:
        """
        Retrieve video IDs from a specific channel
        """
        video_ids = []
        request = self.youtube.search().list(
            part="id",
            channelId=channel_id,
            maxResults=max_results,
            order="date",
            type="video"
        )
        response = request.execute()

        for item in response.get("items", []):
            video_ids.append(item["id"]["videoId"])

        print(f"✓ Found {len(video_ids)} videos for channel ID: {channel_id}")
        return video_ids

    def get_video_comments(self, video_id: str, max_comments: int = 500) -> List[Dict]:
        """
        Collect comments for a given video
        """
        comments = []
        try:
            request = self.youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                textFormat="plainText"
            )
            while request and len(comments) < max_comments:
                response = request.execute()

                for item in response.get("items", []):
                    snippet = item["snippet"]["topLevelComment"]["snippet"]
                    comment_data = {
                        "video_id": video_id,
                        "comment_id": item["id"],
                        "author": snippet.get("authorDisplayName"),
                        "text": snippet.get("textDisplay"),
                        "published_at": snippet.get("publishedAt"),
                        "like_count": snippet.get("likeCount"),
                        "reply_count": item["snippet"].get("totalReplyCount", 0)
                    }
                    comments.append(comment_data)

                # Pagination
                if "nextPageToken" in response:
                    request = self.youtube.commentThreads().list(
                        part="snippet",
                        videoId=video_id,
                        maxResults=100,
                        pageToken=response["nextPageToken"],
                        textFormat="plainText"
                    )
                else:
                    break

            print(f"  ✓ Collected {len(comments)} comments for video {video_id}")

        except Exception as e:
            print(f"✗ Error fetching comments for {video_id}: {e}")

        return comments

    def collect_from_channels(self, channel_ids: Dict[str, str],
                              max_videos_per_channel: int = 10,
                              max_comments_per_video: int = 500) -> List[Dict]:
        """
        Collect comments from multiple news channels
        """
        all_comments = []
        for channel_name, channel_id in channel_ids.items():
            print(f"\n📺 Collecting from {channel_name}...")
            video_ids = self.get_channel_videos(channel_id, max_videos_per_channel)

            for vid in video_ids:
                video_comments = self.get_video_comments(vid, max_comments_per_video)
                for c in video_comments:
                    c["channel_name"] = channel_name
                all_comments.extend(video_comments)

        print(f"\n✓ Total comments collected: {len(all_comments)}")
        return all_comments

    def save_data(self, data: List[Dict], filename: str = None):
        """
        Save collected data as JSON and CSV
        """
        if not filename:
            filename = f"youtube_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        json_path = os.path.join(self.output_dir, f"{filename}.json")
        csv_path = os.path.join(self.output_dir, f"{filename}.csv")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        pd.DataFrame(data).to_csv(csv_path, index=False, encoding="utf-8")
        print(f"\n✓ Data saved:")
        print(f"  JSON → {json_path}")
        print(f"  CSV  → {csv_path}")
        print(f"  Total comments: {len(data)}")


def main():
    """
    Collect YouTube comments on Israel–Hamas War from news channels
    """
    print("=" * 60)
    print("YOUTUBE DATA COLLECTION")
    print("=" * 60)

    collector = YouTubeCollector(API_KEY)

    # Popular news channels (replace with actual IDs)
    CHANNEL_IDS = {
        "BBC": "UC16niRr50-MSBwiO3YDb3RA",
        "Aljazeera": "UCNye-wNBqNL5ZzHSJj3l8Bg",
        "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
        "WION": "UC_gUM8rL-Lrg6O3adPW9K1g",
        "Reuters": "UCZLZ8Jjx_RN2CXloOmgTHVg"
    }

    comments = collector.collect_from_channels(
        channel_ids=CHANNEL_IDS,
        max_videos_per_channel=10,
        max_comments_per_video=500
    )

    collector.save_data(comments, filename="youtube_israel_palestine")

    print("\n" + "=" * 60)
    print("COLLECTION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    # Before running:
    # pip install google-api-python-client python-dotenv pandas
    # and create a .env file with: YOUTUBE_API_KEY=your_api_key
    main()
