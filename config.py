"""
Configuration Template
For Reddit + YouTube Data Collection
Based on the Israel–Hamas War Social Media Analysis Papers
"""

# ============================================================================
# YOUTUBE API CREDENTIALS
# Get from: https://console.cloud.google.com/apis/credentials
# ============================================================================
YOUTUBE_CONFIG = {
    "YOUTUBE_API_KEY": "YOUR_YOUTUBE_API_KEY",  # Replace with your YouTube Data API v3 key
    "YOUTUBE_API_SERVICE_NAME": "youtube",
    "YOUTUBE_API_VERSION": "v3",
}

# YouTube channels to collect from (based on the paper and related sources)
YOUTUBE_CHANNELS = {
    "BBC": "UC16niRr50-MSBwiO3YDb3RA",
    "Aljazeera": "UCNye-wNBqNL5ZzHSJj3l8Bg",
    "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
    "WION": "UC_gUM8rL-Lrg6O3adPW9K1g",
    "Reuters": "UCZLZ8Jjx_RN2CXloOmgTHVg"
}

# YouTube collection settings
YOUTUBE_COLLECTION = {
    "max_videos_per_channel": 10,   # Number of latest videos to fetch per channel
    "max_comments_per_video": 500,  # Max comments per video
    "include_replies": True,        # Whether to collect replies to comments
    "language_filter": ["en"],      # Collect only English comments
}

# ============================================================================
# REDDIT API CREDENTIALS
# Get from: https://www.reddit.com/prefs/apps
# ============================================================================
REDDIT_CONFIG = {
    "REDDIT_CLIENT_ID": "YOUR_CLIENT_ID",
    "REDDIT_CLIENT_SECRET": "YOUR_CLIENT_SECRET",
    "REDDIT_USER_AGENT": "palestine_research_collector"
}

# Reddit subreddits to collect from
REDDIT_SUBREDDITS = [
    "Palestine",
    "Israel",
    "IsraelPalestine",
    "worldnews",
    "news",
    "MiddleEastNews",
    "geopolitics"
]

# Reddit keywords to search for
REDDIT_KEYWORDS = [
    "Palestine",
    "Gaza",
    "Israel",
    "Hamas",
    "IDF",
    "West Bank",
    "Gaza Strip",
    "Israeli occupation"
]

# ============================================================================
# DATA COLLECTION SETTINGS
# ============================================================================

# Date range (as used in the papers: October 7, 2023 – January 20, 2025)
DATE_RANGE = {
    "start_date": "2023-10-07",
    "end_date": "2025-01-20"
}

# Collection limits
COLLECTION_LIMITS = {
    "reddit": {
        "posts_per_subreddit": 5000,
        "max_total_posts": 20000,
        "comments_per_post": 100
    },
    "youtube": {
        "videos_per_channel": 10,
        "max_comments_per_video": 500
    }
}

# ============================================================================
# OUTPUT SETTINGS
# ============================================================================
OUTPUT_CONFIG = {
    "output_dir": "collected_data",
    "save_formats": ["json", "csv"],  # Available: json, csv, parquet
    "create_backup": True,
    "compress_output": False  # Gzip compression
}

# ============================================================================
# COLLECTION BEHAVIOR
# ============================================================================
COLLECTION_CONFIG = {
    "delay_between_requests": 1,  # seconds
    "retry_attempts": 3,
    "timeout": 30,  # seconds
    "verify_ssl": True,
    "save_frequency": 1000,  # Save after every N records
    "log_level": "INFO"  # DEBUG, INFO, WARNING, ERROR
}

# ============================================================================
# FILTERING OPTIONS
# ============================================================================
FILTER_CONFIG = {
    "languages": ["en", "ar", "he"],  # Empty list = all languages
    "min_text_length": 10,  # Minimum characters
    "verified_only": False  # For YouTube verified channels only
}

# ============================================================================
# ANALYSIS SETTINGS (for future use)
# ============================================================================
ANALYSIS_CONFIG = {
    "enable_sentiment": True,
    "enable_topic_modeling": True,
    "enable_entity_extraction": True,
    "sentiment_model": "vader",  # vader, textblob, or transformers
    "topic_model": "bertopic",  # bertopic or lda
    "num_topics": 10
}

# ============================================================================
# SAFETY & ETHICS
# ============================================================================
ETHICS_CONFIG = {
    "anonymize_users": True,  # Remove or hash usernames
    "exclude_personal_info": True,  # Filter out phone numbers, emails
    "respect_robots_txt": True,
    "rate_limit_respect": True,
    "terms_of_service_acknowledged": False  # Set to True after reading ToS
}
