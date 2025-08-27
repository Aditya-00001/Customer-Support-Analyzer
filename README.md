# 🎫 Customer Support Ticket Analytics Dashboard

An **end-to-end NLP-powered ticket analytics dashboard** that processes customer support tickets and provides insights like sentiment analysis, ticket categorization, and trending keywords.

---

## 🚀 Features

* **Ticket Processing**

  * Predicts **category**, **sentiment**, and **emotion** for each support ticket.
* **Dashboard**

  * 📋 Table view of all processed tickets.
  * 📊 Charts and visualizations:

    * Pie chart: % tickets per category
    * Line chart: Sentiment trend over time
    * Word cloud: Frequent keywords/topics
* **Backend API** (Flask)

  * `/tickets`: Get all processed tickets
  * `/summary`: Get aggregated metrics

---

## 🛠️ Tech Stack

* **Backend**: Flask, NLP Pipeline (custom models), Pandas
* **Frontend**: React, Recharts, React-Wordcloud
* **Database**: CSV / can be extended to SQL/NoSQL
* **Others**: Python, JavaScript

---

## 📂 Project Structure

```
project-root/
│── backend/
│   ├── app.py                # Flask backend API
│   ├── models/
│   │   └── NLP_pipeline.py   # Ticket classification + sentiment pipeline
│   ├── data/
│   │   └── processed_data_sample.csv
│   └── requirements.txt      # Backend dependencies
│
│── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── TicketTable.jsx
│   │   │   ├── Charts.jsx
│   │   │   └── WordCloudChart.jsx
│   │   ├── App.js
│   │   └── index.js
│   └── package.json          # Frontend dependencies
│
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Backend runs on: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 2️⃣ Frontend (React)

```bash
cd frontend
npm install
npm start
```

Frontend runs on: **[http://localhost:3000](http://localhost:3000)**

---

## 📊 API Endpoints

### 🔹 Get All Tickets

```http
GET /tickets
```

**Response:**

```json
[
  {
    "query": "Need refund for my order",
    "category": "Refund",
    "sentiment": "Negative",
    "emotion": "Angry"
  }
]
```

### 🔹 Get Summary

```http
GET /summary
```

**Response:**

```json
{
  "category_distribution": {"Refund": 40, "Payment": 30, "Delivery": 20},
  "sentiment_trend": [
    {"date": "2025-08-01", "positive": 10, "negative": 5},
    {"date": "2025-08-02", "positive": 8, "negative": 7}
  ],
  "top_keywords": ["refund", "delay", "payment"]
}
```

---


## 📌 Future Improvements

* Integrate with real **databases** (Postgres/MongoDB)
* Live ticket ingestion via **Kafka/Message Queue**
* Multi-language support in NLP pipeline
* Authentication & Role-based dashboards

---

## 👨‍💻 Author

* **Aditya Narayan Jena**
