
import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [metrics, setMetrics] = useState({});
  const [transactions, setTransactions] = useState([]);

  const API =
  "https://YOUR-CODESPACE-URL-8000.app.github.dev";

  useEffect(() => {

    fetchData();

    const interval = setInterval(
      fetchData,
      5000
    );

    return () => clearInterval(interval);

  }, []);

  const fetchData = async () => {

    try {

      const metricsResponse =
        await axios.get(
          `${API}/metrics`
        );

      const transactionsResponse =
        await axios.get(
          `${API}/transactions`
        );

      setMetrics(
        metricsResponse.data
      );

      setTransactions(
        transactionsResponse.data
      );

    } catch (error) {

      console.error(error);

    }
  };

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial"
      }}
    >

      <h1>
        🚨 Real-Time Fraud Detection Dashboard
      </h1>

      <div
        style={{
          display: "flex",
          gap: "30px",
          marginBottom: "30px"
        }}
      >

        <div>
          <h3>Total Transactions</h3>
          <h2>
            {metrics.total_transactions}
          </h2>
        </div>

        <div>
          <h3>Fraud Alerts</h3>
          <h2>
            {metrics.fraud_alerts}
          </h2>
        </div>

        <div>
          <h3>Fraud Rate</h3>
          <h2>
            {metrics.fraud_rate}%
          </h2>
        </div>

        <div>
          <h3>Average Risk Score</h3>
          <h2>
            {metrics.avg_risk_score}
          </h2>
        </div>

      </div>

      <h2>Recent Transactions</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
          borderCollapse: "collapse",
          width: "100%"
        }}
      >
        <thead>

          <tr>
            <th>ID</th>
            <th>Amount</th>
            <th>Merchant</th>
            <th>Hour</th>
            <th>Risk Score</th>
            <th>Prediction</th>
          </tr>

        </thead>

        <tbody>

          {transactions.map(
            (tx) => (

              <tr key={tx.id}>

                <td>{tx.id}</td>

                <td>
                  {tx.amount}
                </td>

                <td>
                  {tx.merchant_id}
                </td>

                <td>
                  {tx.hour}
                </td>

                <td>
                  {tx.risk_score}
                </td>

                <td>
                  {tx.prediction}
                </td>

              </tr>

            )
          )}

        </tbody>

      </table>

    </div>
  );
}

export default App;

