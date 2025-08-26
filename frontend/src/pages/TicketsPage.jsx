import React, { useEffect, useState } from "react";
import TicketTable from "../components/TicketTable";

function TicketsPage() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    // Fetch tickets from backend
    fetch("http://localhost:5000/tickets") // update if your backend port differs
      .then((res) => res.json())
      .then((data) => setTickets(data))
      .catch((err) => console.error("Error fetching tickets:", err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Customer Tickets</h1>
      <TicketTable tickets={tickets} />
    </div>
  );
}

export default TicketsPage;

