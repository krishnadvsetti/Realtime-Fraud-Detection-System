import { useEffect, useState } from "react";
import { Container, CircularProgress, Alert } from "@mui/material";

import Navbar from "./components/Navbar";
import DashboardCards from "./components/DashboardCards";
import FraudPieChart from "./components/FraudPieChart";
import TransactionsTable from "./components/TransactionsTable";
import LiveStatus from "./components/LiveStatus";
import Footer from "./components/Footer";

import axios from "axios";

const API =
  "https://friendly-invention-xr5gvxgg7w9wc6wq7-8000.app.github.dev";

function App() {
  const [metrics, setMetrics] = useState(null);
  const [summary, setSummary] = useState([]);
  const [transactions, setTransactions] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadDashboard = async () => {
    try {
      const [m, s, t] = await Promise.all([
        axios.get(`${API}/metrics`),
        axios.get(`${API}/fraud-summary`),
        axios.get(`${API}/transactions`),
      ]);

      setMetrics(m.data);
      setSummary(s.data);
      setTransactions(t.data);

      setLoading(false);
      setError("");
    } catch (err) {
      console.error(err);
      setLoading(false);
      setError("Unable to connect to backend.");
    }
  };

  useEffect(() => {
    loadDashboard();

    const interval = setInterval(loadDashboard, 5000);

    return () => clearInterval(interval);
  }, []);

  if (loading)
    return (
      <Container sx={{ mt: 10, textAlign: "center" }}>
        <CircularProgress />
      </Container>
    );

  if (error)
    return (
      <Container sx={{ mt: 5 }}>
        <Alert severity="error">{error}</Alert>
      </Container>
    );

  return (
    <>
      <Navbar />

      <Container maxWidth="xl">
        <LiveStatus />

        <DashboardCards metrics={metrics} />

        <FraudPieChart summary={summary} />

        <TransactionsTable transactions={transactions} />

        <Footer />
      </Container>
    </>
  );
}

export default App;