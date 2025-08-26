import React from "react";
import { PieChart, Pie, Cell, Tooltip, LineChart, Line, XAxis, YAxis, CartesianGrid, Legend } from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#d45087"];

const Charts = ({ summary }) => {
  // Check if summary and its nested properties exist before proceeding
  if (!summary || !summary.category_counts || !summary.sentiment_over_time) {
    return <p>Loading charts...</p>;
  }

  // Transform category counts from a dictionary to an array for the PieChart
  const categoryData = Object.entries(summary.category_counts).map(([category, count]) => ({
  category,
  count,
}));

  // Transform sentiment over time from a nested dictionary to an array for the LineChart
  const sentimentTrendsData = Object.entries(summary.sentiment_over_time).map(([date, sentiments]) => ({
  date,
  ...sentiments,
}));

  return (
    <div className="grid grid-cols-2 gap-6 p-6">
      {/* Pie Chart */}
      <div className="shadow-lg rounded-xl p-4 border">
        <h2 className="text-lg font-bold mb-2">Tickets per Category</h2>
        <PieChart width={400} height={300}>
          <Pie
            data={categoryData}
            dataKey="count"
            nameKey="category"
            cx="50%"
            cy="50%"
            outerRadius={100}
            label
          >
            {categoryData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </div>

      {/* Line Chart */}
      <div className="shadow-lg rounded-xl p-4 border">
        <h2 className="text-lg font-bold mb-2">Sentiment Trend Over Time</h2>
        <LineChart width={500} height={300} data={sentimentTrendsData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="positive" stroke="#00C49F" />
          <Line type="monotone" dataKey="negative" stroke="#FF8042" />
          <Line type="monotone" dataKey="neutral" stroke="#0088FE" />
        </LineChart>
      </div>
    </div>
  );
};

export default Charts;
