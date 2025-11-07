# 🤖 AI + PCOD Social Media Insight Analyzer

This project uses **Natural Language Processing (NLP)** and **unsupervised clustering** to uncover key themes, emotions, and sentiments in online discussions related to **Polycystic Ovarian Disease (PCOD)**. The final output is an **interactive Streamlit dashboard** that helps researchers and clinicians explore cluster-wise insights and narratives around PCOD.

---

## 📌 Objectives

- Analyze PCOD-related social media posts to identify emerging themes.
- Apply sentiment and emotion classification using transformer-based models.
- Use embeddings + clustering to group semantically similar posts.
- Generate human-readable **insight cards** with summaries and word clouds.
- Build a user-friendly dashboard for exploratory analysis.

---

## ✅ What We've Done

- Collected and cleaned PCOD-related social media posts (e.g., Reddit).
- Applied sentiment and emotion models using Hugging Face transformers.
- Embedded text using `all-mpnet-base-v2` and `BAAI/bge-base-en-v1.5`.
- Performed clustering using **KMeans** and **HDBSCAN** after UMAP reduction.
- Extracted top keywords per cluster via **TF-IDF**.
- Created **GPT-generated insight cards** per cluster.
- Designed a **Streamlit dashboard** for interactive exploration.

---

## 🧠 Methods Used

| Task                     | Tools / Libraries                                    |
|--------------------------|------------------------------------------------------|
| Data Cleaning            | `pandas`, `re`, `nltk`                               |
| Sentiment Analysis       | `cardiffnlp/twitter-roberta-base-sentiment`          |
| Emotion Classification   | `j-hartmann/emotion-english-distilroberta-base`     |
| Embeddings               | `sentence-transformers`, `BAAI`, `all-mpnet-base-v2` |
| Dimensionality Reduction | `UMAP`                                               |
| Clustering               | `KMeans`, `HDBSCAN`                                  |
| Keyword Extraction       | `TfidfVectorizer`                                    |
| Summarization            | `GPT` / `ChatGPT`                                    |
| Visualization            | `WordCloud`, `matplotlib`, `Streamlit`               |

---

## 💡 Dashboard Features

Launch the dashboard via:

```bash
streamlit run app/dashboard.py


## Installation
git clone https://github.com/your-username/pcod-nlp-insights.git
cd pcod-nlp-insights
pip install -r requirements.txt
streamlit run app/dashboard.py