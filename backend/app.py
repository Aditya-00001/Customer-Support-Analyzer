from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # allow requests from frontend

# Load dataset
df = pd.read_csv("data/twcs.csv")

@app.route("/data", methods=["GET"])
def get_data():
    """Return first 10 rows for preview"""
    sample = df.head(10).to_dict(orient="records")
    return jsonify(sample)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

