"""
Configuration Template
"""

# ============================================================================
# TELEGRAM API CREDENTIALS
# Get from: https://my.telegram.org
# ============================================================================
TELEGRAM_CONFIG = {
    "api_id": "YOUR_API_ID",  # e.g., 12345678
    "api_hash": "YOUR_API_HASH",  # e.g., "0123456789abcdef0123456789abcdef"
    "phone": "YOUR_PHONE_NUMBER",  # e.g., "+1234567890" (with country code)
}

# Telegram channels to collect from (from the paper)
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

# ============================================================================
# TWITTER/X API CREDENTIALS (Optional - snscrape doesn't need API)
# Get from: https://developer.twitter.com
# ============================================================================
TWITTER_CONFIG = {
    "api_key": "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET",
}

# Twitter keywords to search for
TWITTER_KEYWORDS = [
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

# ============================================================================
# REDDIT API CREDENTIALS
# Get from: https://www.reddit.com/prefs/apps
# ============================================================================
REDDIT_CONFIG = {
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "user_agent": "palestine_research_collector v1.0 by /u/YOUR_USERNAME"
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

# Date range (from the paper: October 23, 2023 - January 20, 2025)
DATE_RANGE = {
    "start_date": "2023-10-23",
    "end_date": "2025-01-20"
}

# Collection limits
COLLECTION_LIMITS = {
    "telegram": {
        "messages_per_channel": None,  # None = unlimited
        "max_total_messages": 150000
    },
    "twitter": {
        "tweets_per_keyword": 2000,
        "max_total_tweets": 10000
    },
    "reddit": {
        "posts_per_subreddit": 5000,
        "max_total_posts": 20000,
        "comments_per_post": 100
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
    "save_frequency": 1000,  # Save after every N messages
    "log_level": "INFO"  # DEBUG, INFO, WARNING, ERROR
}

# ============================================================================
# FILTERING OPTIONS
# ============================================================================
FILTER_CONFIG = {
    "languages": ["en", "ar", "he"],  # Empty list = all languages
    "min_text_length": 10,  # Minimum characters
    "exclude_retweets": False,
    "exclude_replies": False,
    "verified_only": False  # Only verified accounts
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
