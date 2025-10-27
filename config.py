"""
Configuration file for Social Media Data Collection
(Used by reddit_collector.py and youtube_collector.py)
"""

from datetime import datetime

# ==========================================================
# 🟥 REDDIT CONFIGURATION
# ==========================================================

# Subreddits related to geopolitical and Middle East discussions
SUBREDDITS = [
    "Palestine",
    "Israel",
    "IsraelPalestine",
    "worldnews",
    "news",
    "MiddleEastNews",
    "geopolitics"
]

# Conflict-related keywords
REDDIT_KEYWORDS = [
    "Palestine",
    "Gaza",
    "Israel",
    "Hamas",
    "IDF",
    "West Bank",
    "Gaza Strip",
    "Israeli occupation",
    "Middle East conflict"
]

# Maximum posts to collect per subreddit
MAX_POSTS_PER_SUB = 2000  # Increase for larger datasets

# ==========================================================
# 🟥 YOUTUBE CONFIGURATION
# ==========================================================

# Channel IDs of major international news outlets
YOUTUBE_CHANNELS = {
    "BBC News": "UC16niRr50-MSBwiO3YDb3RA",
    "Al Jazeera English": "UCNye-wNBqNL5ZzHSJj3l8Bg",
    "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
    "Reuters": "UCZLZ8Jjx_RN2CXloOmgTHVg",
    "WION": "UC_gUM8rL-Lrg6O3adPW9K1g"
}

# Keywords to filter YouTube videos
YOUTUBE_KEYWORDS = [
    "Israel",
    "Palestine",
    "Gaza",
    "Hamas",
    "IDF",
    "Middle East",
    "Conflict",
    "War",
    "Ceasefire",
    "Jerusalem"
]

# Collection limits
MAX_VIDEOS_PER_CHANNEL = 10   # number of videos per channel
MAX_COMMENTS_PER_VIDEO = 500  # number of comments per video

# ==========================================================
# 🗂️ OUTPUT CONFIGURATION
# ==========================================================

# Directory to save all collected data
OUTPUT_DIR = "collected_data"

# Filename templates
REDDIT_OUTPUT_FILE = "reddit_israel_palestine"
YOUTUBE_OUTPUT_FILE = "youtube_israel_palestine"

# ==========================================================
# 🕒 DATE RANGE (for labeling or filtering during analysis)
# ==========================================================

# Even though Reddit & YouTube collect latest data,
# you can still define time range for reference in analysis.
START_DATE = datetime(2023, 10, 7)   # Conflict start date
END_DATE = datetime(2025, 1, 20)     # Latest collection date

