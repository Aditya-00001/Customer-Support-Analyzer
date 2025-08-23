import pandas as pd
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import spacy
from bertopic import BERTopic

# Load dataset
df = pd.read_csv("data/sample_small.csv")

# -------------------------
# 1. Automated Query Classification (Clustering)
# -------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(df["text"].astype(str).tolist(), show_progress_bar=True)

kmeans = KMeans(n_clusters=5, random_state=42)
df["predicted_category"] = kmeans.fit_predict(embeddings)

# -------------------------
# 2. Sentiment & Emotion Analysis
# -------------------------
sentiment_analyzer = pipeline("sentiment-analysis")
df["sentiment"] = df["text"].astype(str).apply(lambda x: sentiment_analyzer(x[:512])[0]['label'])

emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
df["emotion"] = df["text"].astype(str).apply(lambda x: emotion_analyzer(x[:512])[0]['label'])

# -------------------------
# 3. Entity Extraction (NER)
# -------------------------
nlp = spacy.load("en_core_web_sm")
def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

df["entities"] = df["text"].astype(str).apply(extract_entities)

# -------------------------
# 4. Topic Modeling
# -------------------------
topic_model = BERTopic()
topics, _ = topic_model.fit_transform(df["text"].astype(str).tolist())
df["topic"] = topics

# -------------------------
# Save Processed Data
# -------------------------
df.to_csv("data/processed_data_sample.csv", index=False)
print("✅ NLP processing complete. Saved to data/processed.csv")
