import React, { useEffect, useState } from "react";

const TicketTable = () => {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/tickets") // adjust if backend runs on different port
      .then((res) => res.json())
      .then((data) => setTickets(data));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">All Tickets</h2>
      <table className="w-full border-collapse border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-2">Query</th>
            <th className="border p-2">Category</th>
            <th className="border p-2">Sentiment</th>
            <th className="border p-2">Emotion</th>
          </tr>
        </thead>
        <tbody>
          {tickets.map((ticket, idx) => (
            <tr key={idx} className="hover:bg-gray-50">
              <td className="border p-2">{ticket.query}</td>
              <td className="border p-2">{ticket.predicted_category}</td>
              <td className="border p-2">{ticket.sentiment}</td>
              <td className="border p-2">{ticket.emotion}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TicketTable;

