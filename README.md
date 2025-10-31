# 📊 Social Media Data Collection for Israel–Hamas War Analysis

This project replicates and extends the data collection methodology from key research papers analyzing online discourse about the **Israel–Hamas war**, focusing on **Reddit**, **YouTube**, and **Telegram**.

---

## 🧠 Research Basis

Inspired by:

* **“Israel–Hamas war through Telegram, Reddit and Twitter”** — Despoina Antonakaki & Sotiris Ioannidis (2025)
* **“Sentiment analysis of the Hamas–Israel war on YouTube”** (2025)

This project collects and analyzes social media data to study **public discourse, sentiment, and topic prevalence** across major online platforms during the Israel–Hamas conflict.

---

## 🪄 Platforms Covered

* **Reddit (Public JSON API)** — Latest and historical posts from conflict-related subreddits
* **YouTube (YouTube Data API v3)** — Video metadata + comments from verified news channels, filtered by keywords
* **Telegram (Telethon)** — Public channel messages within a specific date range

---

## ⚙️ Setup Instructions

### 1️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 2️⃣ API Credentials & Environment Setup

Create a `.env` file in your project root:

```env
# YouTube
YOUTUBE_API_KEY=your_youtube_api_key

# Telegram
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=+91xxxxxxxxxx
```

✅ **Reddit:** no credentials needed — it uses Reddit’s public JSON endpoints.

---

## 📁 File Structure

```
CSS/
├── reddit_collector.py          # Reddit data collection (Public JSON)
├── youtube_collector.py         # YouTube data collection (API + keywords)
├── telegram_collector.py        # Telegram data collection (Telethon + date filter)
├── config.py                    # Central configuration file
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
└── collected_data/              # Output directory
    ├── reddit_israel_palestine.json
    ├── youtube_israel_palestine.json
    ├── telegram_israel_palestine.json
```

---

## 🚀 Usage Guide

### 🟥 Step 1 — Reddit Data Collection

```bash
python reddit_collector.py
```

**Fetches:** Recent Reddit posts containing conflict-related keywords from targeted subreddits.

---

### 🟦 Step 2 — YouTube Data Collection

```bash
python youtube_collector.py
```

**Fetches:** Videos and comments matching Israel–Hamas war keywords from trusted news channels.

---

### 🟩 Step 3 — Telegram Data Collection

```bash
python telegram_collector.py
```

**Fetches:** Messages from public Telegram channels (e.g., GazaNow, EyeOnPalestine, TimesOfGaza) within the defined date range.

---

## 📊 Data Collection Details

### 🟥 Reddit

**Subreddits:**
`Palestine`, `Israel`, `IsraelPalestine`, `worldnews`, `news`, `MiddleEastNews`, `geopolitics`

**Keywords:**
`Palestine`, `Gaza`, `Israel`, `Hamas`, `IDF`, `West Bank`, `Israeli occupation`, `Gaza Strip`

**Fields:**

| Field        | Description           |
| ------------ | --------------------- |
| post_id      | Unique Reddit post ID |
| subreddit    | Source subreddit      |
| author       | Username (if public)  |
| date         | UTC post timestamp    |
| title        | Post title            |
| text         | Post body             |
| score        | Upvotes               |
| num_comments | Number of comments    |
| upvote_ratio | Upvote ratio          |
| keyword      | Matched keyword       |

---

### 🟦 YouTube

**Channels:** BBC News | Al Jazeera English | CNN | Reuters | WION

**Keywords:**
`Israel`, `Hamas`, `Palestine`, `Gaza`, `Conflict`, `War`, `Ceasefire`, `Jerusalem`, `Middle East`, `IDF`

**Fields:**

| Field          | Description        |
| -------------- | ------------------ |
| video_id       | YouTube video ID   |
| channel_name   | Source channel     |
| video_title    | Title              |
| published_date | Upload date        |
| description    | Video description  |
| comment_text   | Individual comment |
| comment_author | Comment author     |
| comment_date   | Comment timestamp  |
| like_count     | Comment likes      |
| reply_count    | Replies            |
| keyword        | Matched keyword    |

---

### 🟩 Telegram

**Channels Monitored:**
`GazaNow`, `EyeonPalestine`, `TimesOfGaza`, `AlMayadeenNews`, `MiddleEastMonitor`, `Jerusalem_Post`, `BBCBreaking`, and others.

**Date Range:** `2023-10-07 → 2025-01-20`

**Fields:**

| Field      | Description             |
| ---------- | ----------------------- |
| channel    | Source Telegram channel |
| message_id | Unique message ID       |
| date       | UTC timestamp           |
| text       | Message content         |
| views      | Number of views         |
| forwards   | Number of forwards      |
| replies    | Number of replies       |
| link       | Direct message URL      |

---

## 📁 Output Examples

### Reddit (JSON)

```json
{
  "post_id": "abc123",
  "subreddit": "worldnews",
  "title": "Israel–Hamas conflict intensifies",
  "text": "Latest updates from Gaza...",
  "score": 512,
  "num_comments": 74,
  "keyword": "Israel"
}
```

### YouTube (JSON)

```json
{
  "video_id": "xyz789",
  "channel_name": "BBC News",
  "video_title": "Israel–Hamas Conflict Update",
  "comment_text": "Praying for peace",
  "comment_date": "2024-11-15T10:30:00",
  "keyword": "Gaza"
}
```

### Telegram (JSON)

```json
{
  "channel": "TimesOfGaza",
  "message_id": 12345,
  "date": "2024-10-12T09:15:00Z",
  "text": "Breaking: ceasefire discussions underway.",
  "views": 15800,
  "forwards": 120,
  "replies": 6,
  "link": "https://t.me/TimesOfGaza/12345"
}
```

---

## 📈 Next Steps — Analysis

1. **Sentiment Analysis** – `VADER`, `TextBlob`, or Hugging Face models
2. **Topic Modeling** – `LDA`, `BERTopic`, `Top2Vec`
3. **Entity Extraction** – Identify people, places, organizations
4. **Trend Analysis** – Measure narrative shifts over time
5. **Cross-Platform Comparison** – Contrast Reddit vs YouTube vs Telegram tone and reach

---

## ⚠️ Important Notes

* Reddit: 1-second delay per request
* YouTube: 10 000-unit daily quota
* Telegram: public data only; avoid private groups

🛡️ **Ethics:** Collect only public data, respect each platform’s Terms of Service, and anonymize user information before analysis or publication.

---

## 📚 References

* *Israel–Hamas war through Telegram, Reddit and Twitter* — Despoina Antonakaki & Sotiris Ioannidis (2025)
* *Sentiment analysis of the Hamas–Israel war on YouTube* — arXiv (2025)

---

## 📄 License

This project is for **research and educational use only**.
If you build upon this work, please cite the original research papers and this implementation.
