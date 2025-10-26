# Social Media Data Collection for Israel-Hamas War Analysis

This project replicates the data collection methodology from the research paper "Israel–Hamas war through Telegram, Reddit and Twitter" by Despoina Antonakaki and Sotiris Ioannidis.

## 📊 Paper Overview

The paper analyzes online discussions about the Israeli-Palestinian conflict across three platforms:

- **Telegram**: 125,054 messages from 20 channels (Oct 23, 2023 - Jan 20, 2025)
- **Twitter**: 2,001 tweets
- **Reddit**: 2 million opinions

### Key Findings from the Paper:

- Polarized narratives across platforms
- Sentiment-topic prevalence analysis
- Entity extraction and BERT topic modeling
- Volume analysis and emotional tone tracking

## 🛠️ Setup Instructions

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 2. Get API Credentials

#### Telegram API

1. Visit https://my.telegram.org
2. Login with your phone number
3. Go to "API development tools"
4. Create an application
5. Save your `api_id` and `api_hash`

#### Twitter/X (Optional - uses snscrape instead)

1. Visit https://developer.twitter.com
2. Apply for developer access
3. Create a project and app
4. Save your API keys

#### Reddit API

1. Visit https://www.reddit.com/prefs/apps
2. Click "create another app"
3. Select "script"
4. Save your `client_id` and `client_secret`

## 📁 File Structure

```
CSS/
├── data_collection_script.py      # Main setup script
├── telegram_collector.py          # Telegram data collection
├── twitter_collector.py           # Twitter data collection
├── reddit_collector.py            # Reddit data collection
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── collected_data/                # Output directory
    ├── telegram_config.json
    ├── twitter_config.json
    ├── reddit_config.json
    └── [collected data files]
```

## 🚀 Usage

### Quick Start - Setup Configuration

Run this first to create configuration files:

```bash
python data_collection_script.py
```

This will create configuration files in the `collected_data` folder.

### Collect Telegram Data

1. Edit `telegram_collector.py` and add your credentials:

```python
API_ID = "your_api_id"
API_HASH = "your_api_hash"
PHONE = "+1234567890"
```

2. Run the collector:

```bash
python telegram_collector.py
```

### Collect Twitter Data

The Twitter collector uses `snscrape` (no API key needed):

```bash
python twitter_collector.py
```

### Collect Reddit Data

1. Edit `reddit_collector.py` and add your credentials:

```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
```

2. Run the collector:

```bash
python reddit_collector.py
```

## 📋 Data Collection Details

### Telegram Channels (from Paper)

The paper collected from these 20 channels:

- AlQassamBrigades (92,326 messages)
- Eyeonpalestine (27,075 messages)
- FreePalestine2023 (20,231 messages)
- TheJerusalemPost (7,907 messages)
- gazaenglishupdates (34,688 messages)
- And 15 more channels...

### Twitter Keywords

Search terms used:

- #FreePalestine
- #Gaza
- #Israel
- #Palestine
- #IsraelHamas
- "Gaza conflict"
- "Israel Hamas war"

### Reddit Subreddits

Monitored subreddits:

- r/Palestine
- r/Israel
- r/IsraelPalestine
- r/worldnews
- r/news

## 📊 Output Format

All collectors save data in two formats:

### JSON Format

```json
{
  "message_id": "123",
  "channel_name": "example",
  "date": "2024-01-20T10:30:00",
  "text": "Message content...",
  "views": 1000,
  "forwards": 50
}
```

### CSV Format

Same fields in tabular format for easy analysis in Excel/Pandas.

## 🔍 Data Fields

### Telegram

- message_id
- channel_name
- date
- text
- views
- forwards
- replies
- media_type

### Twitter

- tweet_id
- username
- date
- text
- retweet_count
- like_count
- reply_count
- hashtags

### Reddit

- post_id
- subreddit
- author
- date
- title
- text
- score
- num_comments
- upvote_ratio

## 📈 Next Steps - Analysis

After collecting data, you can perform:

1. **Volume Analysis**: Track message frequency over time
2. **Entity Extraction**: Identify key entities mentioned
3. **Topic Modeling**: Use BERTopic or LDA
4. **Sentiment Analysis**: Analyze emotional tone
5. **Network Analysis**: Study information spread patterns

## ⚠️ Important Notes

### Rate Limiting

- Telegram: Built-in 1-second delay between requests
- Twitter: snscrape handles rate limiting automatically
- Reddit: PRAW handles rate limiting automatically

### Privacy & Ethics

- Respect user privacy
- Follow platform Terms of Service
- Only collect public data
- Anonymize personal information
- Use data responsibly

### Data Storage

- Large datasets can be several GB
- Ensure sufficient disk space
- Consider database storage for large collections
- Regularly backup collected data

## 🐛 Troubleshooting

### Telegram Issues

- **Error: Phone number not registered**: Register your phone number with Telegram first
- **Error: API ID invalid**: Double-check your credentials from my.telegram.org
- **Flood wait error**: You're collecting too fast; the script already has delays built-in

### Twitter Issues

- **Error: Module not found**: Install snscrape: `pip install snscrape`
- **No tweets returned**: Try different date ranges or keywords
- **Rate limit**: Wait a few minutes and try again

### Reddit Issues

- **401 Unauthorized**: Check your API credentials
- **429 Too Many Requests**: PRAW handles this automatically, just wait
- **Empty results**: Verify subreddit names and date ranges

## 📚 References

Based on the paper:

- **Title**: Israel–Hamas war through Telegram, Reddit and Twitter
- **Authors**: Despoina Antonakaki, Sotiris Ioannidis
- **Institution**: Technical University of Crete & FORTH
- **Date**: February 4, 2025
- **arXiv**: 2502.00060v1 [cs.SI]

## 📄 License

This code is provided for research and educational purposes. Please cite the original paper if you use this methodology in your research.

## 🤝 Contributing

Feel free to improve this code:

- Add more platforms (TikTok, Facebook, etc.)
- Improve error handling
- Add data validation
- Create analysis scripts

## 📧 Contact

For questions about the original research, contact:

- Despoina Antonakaki: dantonakaki@tuc.gr, despoina@ics.forth.gr

---

**Note**: This implementation is based on the methodology described in the paper. Actual data collection requires valid API credentials and may be subject to platform policies and rate limits.
