import React, { useEffect, useState } from "react";
import Charts from "../components/Charts";
import WordCloudChart from "../components/WordCloudChart";

function DashboardPage() {
  const [summary, setSummary] = useState(null);

  useEffect(() => {
    // Fetch ticket summary from backend
    fetch("http://localhost:5000/summary")
      .then((res) => res.json())
      .then((data) => setSummary(data))
      .catch((err) => console.error("Error fetching summary:", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Ticket Dashboard</h1>
      {summary ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Charts summary={summary} />
          <WordCloudChart summary={summary} />
        </div>
      ) : (
        <p>Loading summary...</p>
      )}
    </div>
  );
}

export default DashboardPage;

