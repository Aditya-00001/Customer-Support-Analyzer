from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Load processed data (from Phase 3 EDA or your pipeline output)
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed_data_sample.csv")
df = pd.read_csv(DATA_PATH)

@app.route("/tickets", methods=["GET"])
def get_tickets():
    """Return all processed tickets"""
    return df.to_dict(orient="records")

@app.route("/summary", methods=["GET"])
def get_summary():
    """Return aggregated metrics for dashboard"""
    summary = {
        "category_counts": df["predicted_category"].value_counts().to_dict(),
        "sentiment_counts": df["sentiment"].value_counts().to_dict(),
        "emotion_counts": df["emotion"].value_counts().to_dict(),
    }
    
    # If time data exists
    if "created_at" in df.columns:
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
        summary["sentiment_over_time"] = (
            df.groupby(df["created_at"].dt.date)["sentiment"]
            .value_counts()
            .unstack(fill_value=0)
            .to_dict()
        )
    
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)

