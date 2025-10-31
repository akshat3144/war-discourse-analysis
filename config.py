"""
Configuration file for Social Media Data Collection
(Used by reddit_collector.py, youtube_collector.py, and telegram_collector.py)
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
MAX_VIDEOS_PER_CHANNEL = 10   # Number of videos per channel
MAX_COMMENTS_PER_VIDEO = 500  # Number of comments per video

# ==========================================================
# 🟦 TELEGRAM CONFIGURATION
# ==========================================================

# Channels known to discuss or report on the Israel–Hamas conflict
TELEGRAM_CHANNELS = [
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

# Maximum messages to collect per channel
MAX_MESSAGES_PER_CHANNEL = 2000

# ==========================================================
# 🗂️ OUTPUT CONFIGURATION
# ==========================================================

# Directory to save all collected data
OUTPUT_DIR = "collected_data"

# Filename templates
REDDIT_OUTPUT_FILE = "reddit_israel_palestine"
YOUTUBE_OUTPUT_FILE = "youtube_israel_palestine"
TELEGRAM_OUTPUT_FILE = "telegram_israel_palestine"

# ==========================================================
# 🕒 DATE RANGE (used for filtering or labeling during analysis)
# ==========================================================

START_DATE = datetime(2023, 10, 7)   # Conflict start date
END_DATE = datetime(2025, 1, 20)     # Latest collection date