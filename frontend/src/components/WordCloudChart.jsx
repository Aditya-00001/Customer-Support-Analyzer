import React from "react";
import { WordCloud } from "@isoterik/react-word-cloud";

const WordCloudChart = ({ summary }) => {
  // Check if summary and its nested properties exist before proceeding
  console.log(summary);
  if (!summary || !summary.emotion_counts) {
    return <p>Loading word cloud...</p>;
  }

  // Map and filter in one step to ensure numeric values are used.
  const words = Object.entries(summary.emotion_counts)
    .map(([emotion, count]) => ({
      text: emotion,
      value: Number(count), // Convert to number here
    }))
    .filter((entry) => typeof entry.value === "number" && !isNaN(entry.value) && entry.value > 0);

  // If there is no valid data, display a message instead of the chart
  if (words.length === 0) {
    return <p>No valid emotion data to display.</p>;
  }

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">Emotions Word Cloud</h2>
      <div style={{ height: 400, width: "100%" }}>
        <WordCloud
          words={words}
          options={{
            rotations: 2,
            rotationAngles: [-90, 0],
            fontSizes: [20, 60],
          }}
        />
      </div>
    </div>
  );
};

export default WordCloudChart;
