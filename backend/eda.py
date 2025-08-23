# Phase 3: EDA & Cross Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load processed dataset
df = pd.read_csv("data/processed_data_sample.csv")
os.makedirs("reports", exist_ok=True)
# -------------------------------
# 1. Topic Distribution
# -------------------------------
plt.figure(figsize=(12,6))
df['topic'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Topic Distribution", fontsize=16)
plt.xlabel("Topic")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/topic_distribution.png")
plt.show()

# -------------------------------
# 2. Sentiment per Predicted Category
# -------------------------------
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='predicted_category', hue='sentiment')
plt.title("Sentiment per Category", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/sentiment_per_category.png")
plt.show()

# -------------------------------
# 3. Emotion per Topic
# -------------------------------
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='topic', hue='emotion')
plt.title("Emotion per Topic", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/emotion_per_topic.png")
plt.show()

# -------------------------------
# 4. Entities → Brands/Keywords with Sentiment
# -------------------------------
# Flatten entities if multiple per tweet
df['entities'] = df['entities'].astype(str)
entity_sentiment = df.groupby(['entities', 'sentiment']).size().unstack(fill_value=0)
top_entities = entity_sentiment.sum(axis=1).sort_values(ascending=False).head(15)

plt.figure(figsize=(12,6))
entity_sentiment.loc[top_entities.index].plot(kind='bar', stacked=True)
plt.title("Top Entities by Sentiment", fontsize=16)
plt.xlabel("Entity")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/entities_sentiment.png")
plt.show()

# -------------------------------
# 5. Time-based Trends
# -------------------------------
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
df['date'] = df['created_at'].dt.date

# Tweets per day
plt.figure(figsize=(12,6))
df.groupby('date').size().plot(kind='line', marker='o')
plt.title("Tweet Volume Over Time", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.savefig("reports/tweets_over_time.png")
plt.show()

# Sentiment over time
plt.figure(figsize=(12,6))
df.groupby(['date','sentiment']).size().unstack(fill_value=0).plot(marker='o')
plt.title("Sentiment Trend Over Time", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.tight_layout()
plt.savefig("reports/sentiment_trend_over_time.png")
plt.show()

# -------------------------------
# 6. Word Clouds for Sentiment/Emotion
# -------------------------------
def plot_wordcloud(subset, title, filename):
    text = " ".join(subset['text'].astype(str))
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.savefig(filename)
    plt.show()

# WordClouds
for sentiment in df['sentiment'].unique():
    plot_wordcloud(df[df['sentiment']==sentiment], f"WordCloud - {sentiment} Sentiment", f"reports/wordcloud_{sentiment}.png")

for emotion in df['emotion'].unique():
    plot_wordcloud(df[df['emotion']==emotion], f"WordCloud - {emotion} Emotion", f"reports/wordcloud_{emotion}.png")

