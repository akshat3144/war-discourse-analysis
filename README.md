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

* **Reddit (Pushshift API)** — Historical and recent posts/comments from conflict-related subreddits
* **YouTube (YouTube Data API v3)** — Video metadata and comments from major international news channels

---

## ⚙️ Setup Instructions

### 1. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 2. Get API Credentials

#### 🟥 YouTube Data API v3

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **new project**
3. Enable the **YouTube Data API v3**
4. Navigate to **APIs & Services → Credentials → Create API key**
5. Copy your API key into `youtube_collector.py`

✅ **Note:**
Reddit collection does **not** require any credentials — it uses the public **Pushshift JSON API**, which allows free access to Reddit’s historical and live data.

---

## 📁 File Structure

```
CSS/
├── data_collection_script.py       # Configuration setup
├── reddit_collector.py             # Reddit data collection (Pushshift JSON-based)
├── youtube_collector.py            # YouTube data collection (YouTube Data API v3)
├── config_template.py              # Configuration for date ranges & parameters
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── collected_data/                 # Output directory
    ├── reddit_israel_palestine.json
    ├── youtube_israel_palestine.json
    └── [collected data files]
```

---

## 🚀 Usage

### Step 1 — Configure Parameters

Edit `config_template.py` to set:

* **Date range**
* **Subreddits**
* **Keywords**
* **Output paths**

---

### Step 2 — Collect Reddit Data

Run the Reddit collector:

```bash
python reddit_collector.py
```

**This uses the Pushshift API** to fetch both historical and live Reddit data, no authentication needed.

---

### Step 3 — Collect YouTube Data

Add your API key to `youtube_collector.py`:

```python
YOUTUBE_API_KEY = "your_api_key"
```

Then run:

```bash
python youtube_collector.py
```

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
`Palestine`, `Gaza`, `Israel`, `Hamas`, `IDF`, `West Bank`, `Israeli occupation`

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
| upvote_ratio | Upvote ratio (if available) |

---

### 🟥 YouTube Collection

**Channels Monitored:**

* BBC News
* Al Jazeera English
* CNN
* Reuters
* WION

**Data Fields:**

| Field          | Description             |
| -------------- | ----------------------- |
| video_id       | YouTube video ID        |
| channel_title  | Channel name            |
| video_title    | Video title             |
| published_date | Video upload date       |
| description    | Video description       |
| view_count     | Total views             |
| like_count     | Likes on the video      |
| comment_count  | Total comments          |
| comment_text   | Individual comment text |
| comment_author | Comment author          |
| comment_date   | Comment timestamp       |

---

## 📁 Output Format

All collectors save in **JSON** and **CSV** formats.

### Example — Reddit JSON

```json
{
  "post_id": "xyz123",
  "subreddit": "worldnews",
  "title": "Israel–Hamas conflict intensifies",
  "text": "Latest updates from Gaza...",
  "score": 512,
  "num_comments": 74,
  "date": "2024-11-15T10:30:00"
}
```

### Example — YouTube JSON

```json
{
  "video_id": "abc123",
  "channel_title": "BBC News",
  "video_title": "Israel–Hamas Conflict Update",
  "comment_text": "Praying for peace",
  "comment_date": "2024-11-15T10:30:00",
  "like_count": 200
}
```

---

## 📈 Next Steps — Analysis

Once data is collected, you can perform:

1. **Sentiment Analysis** — (`VADER`, `TextBlob`, or `transformers`)
2. **Topic Modeling** — (`BERTopic` or `LDA`)
3. **Entity Extraction** — identify names, locations, and organizations
4. **Temporal Trends** — volume and sentiment over time
5. **Platform Comparison** — contrasting narratives between Reddit & YouTube

---

## ⚠️ Important Notes

### Rate Limiting

* Pushshift and YouTube APIs handle rate limits automatically.
* You can configure delays in `reddit_collector.py` (default = 1 second/request).

### Data Ethics

* Collect only **public** data.
* Do not store or publish identifiable user data.
* Follow each platform’s **Terms of Service**.
* Anonymize user identifiers before analysis.

### Storage

* Large datasets can reach several GB depending on date range.
* Store files in `collected_data/` and back them up regularly.

---

## 🐛 Troubleshooting

### Reddit

* **Empty results:** Try shorter date ranges or fewer keywords.
* **HTTP 500 errors:** Pushshift servers can temporarily fail — rerun after a few minutes.
* **Slow response:** Add a small delay (`time.sleep(1)`) between requests.

### YouTube

* **quotaExceeded:** You’ve hit your daily API quota — try again tomorrow.
* **403 errors:** Ensure YouTube Data API v3 is enabled.
* **Missing comments:** Some videos disable comments; the script skips them automatically.

---

## 📚 References

* **Israel–Hamas war through Telegram, Reddit and Twitter** — *Despoina Antonakaki, Sotiris Ioannidis (2025), Technical University of Crete, FORTH*
* **Sentiment analysis of the Hamas–Israel war on YouTube** — *(2025, arXiv preprint)*

---

## 📄 License

This project is for **research and educational purposes only**.
Please cite the original papers if you use this methodology in academic work.

---

## 🤝 Contributing

Contributions welcome for:

* Improved Reddit data filtering
* Sentiment/topic analysis pipelines
* Cross-platform narrative visualization
