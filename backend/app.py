from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os
import numpy as np

app = Flask(__name__)
CORS(app)

# Load processed data
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "processed_data_sample.csv")
df = pd.read_csv(DATA_PATH)

@app.route("/tickets", methods=["GET"])
def get_tickets():
    df_cleaned = df.copy().replace({np.nan: None})
    return jsonify(df_cleaned.to_dict(orient="records"))

@app.route("/summary", methods=["GET"])
def get_summary():
    """Return aggregated metrics for dashboard"""
    # Clean the DataFrame to handle NaN values before aggregation
    df_cleaned = df.copy()
    
    # Fill NaN values in 'emotion' and other categorical columns with a placeholder or drop them
    # Here, we'll ensure they are handled properly
    df_cleaned["emotion"] = df_cleaned["emotion"].fillna("unknown")
    df_cleaned["predicted_category"] = df_cleaned["predicted_category"].fillna("unknown")
    df_cleaned["sentiment"] = df_cleaned["sentiment"].fillna("unknown")

    summary = {
        "category_counts": df_cleaned["predicted_category"].value_counts().to_dict(),
        "sentiment_counts": df_cleaned["sentiment"].value_counts().to_dict(),
        "emotion_counts": df_cleaned["emotion"].value_counts().to_dict(),
    }

    if "created_at" in df_cleaned.columns:
        # Replace 'YOUR_DATE_FORMAT_STRING' with the actual format of your dates
        df_cleaned["created_at"] = pd.to_datetime(
            df_cleaned["created_at"],
            format="%Y-%m-%d %H:%M:%S", # Example format
            errors="coerce"
        )
        
        sentiment_over_time_df = (
            df_cleaned.groupby(df_cleaned["created_at"].dt.date)["sentiment"]
            .value_counts()
            .unstack(fill_value=0)
        )
        sentiment_over_time_df.index = sentiment_over_time_df.index.astype(str)
        summary["sentiment_over_time"] = sentiment_over_time_df.to_dict(orient="index")

    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)
