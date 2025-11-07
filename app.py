import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# === Load the insight cards ===
insights = pd.read_csv("data/pcod_cluster_insight_cards.csv")  # From your GPT step
posts = pd.read_csv("data/kmeans_clustered.csv")  # Original dataset

# === UI Header ===
st.set_page_config(page_title="PCOD Insights Dashboard", layout="wide")
st.title("💡 PCOD Social Media Insight Explorer")
st.markdown("Generated using NLP clustering and GPT summarization")

# === Sidebar filters ===
cluster_names = insights['cluster_name'].tolist()
selected = st.sidebar.selectbox("🔍 Choose a Cluster Theme", cluster_names)

# === Get Selected Cluster Info ===
selected_row = insights[insights['cluster_name'] == selected].iloc[0]
cluster_num = selected_row['cluster']
summary_text = selected_row['summary']

# === Show Insight Card ===
st.markdown(f"### 📌 **Cluster {int(cluster_num)} — {selected}**")
st.info(summary_text)

# === Show Word Cloud ===
# === Show Word Cloud ===
cluster_posts = posts[posts['cluster'] == cluster_num]['cleaned_text']
text_blob = " ".join(cluster_posts)

if text_blob.strip():  # ✅ Prevent error if text is empty
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_blob)
    st.subheader("🗯️ Common Words in this Theme")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
else:
    st.warning("⚠️ No meaningful words found in this cluster to generate a word cloud.")

# === Show sample posts (optional) ===
st.subheader("📝 Example Posts")
sample_df = posts[posts['cluster'] == cluster_num][['cleaned_text', 'dominant_emotion', 'sentiment_label']].head(5)
st.write(sample_df.reset_index(drop=True))