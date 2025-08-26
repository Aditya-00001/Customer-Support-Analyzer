// src/App.jsx
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import TicketsPage from "./pages/TicketsPage";
import DashboardPage from "./pages/DashboardPage";
import './App.css';

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Tickets</Link>
        <Link to="/dashboard">Dashboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<TicketsPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </Router>
  );
}

export default App;
