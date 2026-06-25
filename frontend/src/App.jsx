import { useEffect, useState } from "react";
import { Container, CircularProgress, Alert } from "@mui/material";

import Navbar from "./components/Navbar";
import DashboardCards from "./components/DashboardCards";
import FraudPieChart from "./components/FraudPieChart";
import TransactionsTable from "./components/TransactionsTable";
import LiveStatus from "./components/LiveStatus";
import Footer from "./components/Footer";

import {
  getMetrics,
  getTransactions,
  getFraudSummary,
} from "./services/api";

function App() {
  const [metrics, setMetrics] = useState(null);
  const [summary, setSummary] = useState([]);
  const [transactions, setTransactions] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadDashboard = async () => {
    try {
      

      const [m, s, t] = await Promise.all([
        getMetrics(),
        getFraudSummary(),
        getTransactions(),
      ]);

     


      setMetrics(m.data);
      setSummary(s.data);
      setTransactions(t.data);

      setError("");
    } catch (err) {
      console.error(err);
    
      setError(err.message);
    } finally {
      setLoading(false);
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