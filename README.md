# 📊 Social Media Data Collection for Israel–Hamas War Analysis

This project replicates and extends the data collection methodology from two key research papers analyzing online discussions about the **Israel–Hamas war** — focusing here on **Reddit** and **YouTube**.

---

## 🧠 Research Basis

Inspired by:

* **“Israel–Hamas war through Telegram, Reddit and Twitter”** — Despoina Antonakaki & Sotiris Ioannidis (2025)
* **“Sentiment analysis of the Hamas–Israel war on YouTube”** (2025)

This project collects and analyzes social media data to study **public discourse, sentiment, and topic prevalence** during the Israel–Hamas conflict.

---

## 🪄 Platforms Covered

* **Reddit (Public JSON API)** — Latest posts and discussions from conflict-related subreddits
* **YouTube (YouTube Data API v3)** — Video metadata and comments from **conflict-related videos** filtered by **keywords**

---

## ⚙️ Setup Instructions

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 2. API Credentials

#### 🟥 YouTube Data API v3

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **new project**
3. Enable the **YouTube Data API v3**
4. Navigate to **APIs & Services → Credentials → Create API key**
5. Copy your API key into `youtube_collector.py`:

```python
YOUTUBE_API_KEY = "your_api_key"
```

✅ **Note:**
Reddit collection does **not** require any credentials — it uses Reddit’s **public JSON endpoints**, allowing free access to live data without authentication.

---

## 📁 File Structure

```
CSS/
├── reddit_collector.py             # Reddit data collection (Public JSON API)
├── youtube_collector.py            # YouTube data collection (YouTube Data API v3 + keyword search)
├── config.py                       # Configuration file for future analysis
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── collected_data/                 # Output directory
    ├── reddit_israel_palestine.json
    ├── youtube_israel_palestine.json
    └── [collected data files]
```

---

## 🚀 Usage

### Step 1 — Collect Reddit Data

Run:

```bash
python reddit_collector.py
```

**Fetches:**
Latest Reddit posts from major subreddits using relevant conflict keywords.

---

### Step 2 — Collect YouTube Data

Run:

```bash
python youtube_collector.py
```

**Fetches:**
Latest Videos and comments **matching specific conflict-related keywords** from verified news channels.

---

## 📊 Data Collection Details

### 🟥 Reddit Collection

**Subreddits Monitored:**

* r/Palestine
* r/Israel
* r/IsraelPalestine
* r/worldnews
* r/news
* r/MiddleEastNews
* r/geopolitics

**Keywords:**
`Palestine`, `Gaza`, `Israel`, `Hamas`, `IDF`, `West Bank`, `Gaza Strip`, `Israeli occupation`

**Data Fields:**

| Field        | Description                 |
| ------------ | --------------------------- |
| post_id      | Unique Reddit post ID       |
| subreddit    | Source subreddit            |
| author       | Username (if public)        |
| date         | UTC post creation time      |
| title        | Post title                  |
| text         | Post body content           |
| score        | Upvotes                     |
| num_comments | Number of comments          |
| upvote_ratio | Upvote ratio                |
| keyword      | Search keyword that matched |

---

### 🟥 YouTube Collection

**Channels Monitored:**

* BBC News
* Al Jazeera English
* CNN
* Reuters
* WION

**Keywords Used for Filtering Videos:**
`Israel`, `Hamas`, `Palestine`, `Gaza`, `IDF`, `Middle East`, `Conflict`, `War`, `Ceasefire`, `Jerusalem`

**Data Fields:**

| Field          | Description                    |
| -------------- | ------------------------------ |
| video_id       | YouTube video ID               |
| channel_name   | Channel name                   |
| video_title    | Video title                    |
| published_date | Upload date                    |
| description    | Video description              |
| comment_text   | Individual comment             |
| comment_author | Comment author                 |
| comment_date   | Comment timestamp              |
| like_count     | Likes on comment               |
| reply_count    | Replies to comment             |
| keyword        | Keyword that matched the video |

---

## 📁 Output Format

All collected data is stored in both **JSON** and **CSV** formats.

### Example — Reddit JSON

```json
{
  "post_id": "xyz123",
  "subreddit": "worldnews",
  "title": "Israel–Hamas conflict intensifies",
  "text": "Latest updates from Gaza...",
  "score": 512,
  "num_comments": 74,
  "keyword": "Israel"
}
```

### Example — YouTube JSON

```json
{
  "video_id": "abc123",
  "channel_name": "BBC News",
  "video_title": "Israel–Hamas Conflict Update",
  "comment_text": "Praying for peace",
  "comment_date": "2024-11-15T10:30:00",
  "keyword": "Gaza"
}
```

---

## 📈 Next Steps — Analysis

Once data is collected, you can perform:

1. **Sentiment Analysis** — (`VADER`, `TextBlob`, or `transformers`)
2. **Topic Modeling** — (`BERTopic`, `LDA`)
3. **Entity Recognition** — Detect names, places, and organizations
4. **Temporal Trends** — Compare posting/comment frequency over time
5. **Platform Comparison** — Contrast Reddit vs YouTube narratives

---

## ⚠️ Notes

### Rate Limiting

* Reddit: uses 1-second delay per request
* YouTube: limited by daily API quota (10,000 units/day)

### Data Ethics

* Collect **only public** data
* Respect platform **Terms of Service**
* Remove or anonymize usernames before publication

---

## 📚 References

* **Israel–Hamas war through Telegram, Reddit and Twitter** — *Despoina Antonakaki, Sotiris Ioannidis (2025)*
* **Sentiment analysis of the Hamas–Israel war on YouTube** — *(2025, arXiv preprint)*

---

## 📄 License

This project is for **academic and educational use only**.
Please cite the original papers if you use or extend this work.