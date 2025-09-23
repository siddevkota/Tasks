import React, { useState } from "react";
import AlertBadge from "./AlertBadge";

const initialAlerts = [
  {
    id: 1,
    title: "Database connection failed",
    severity: "critical",
    time: "2025-09-18 08:10",
  },
  {
    id: 2,
    title: "API latency above threshold",
    severity: "high",
    time: "2025-09-18 08:05",
  },
  {
    id: 3,
    title: "Cache miss ratio increased",
    severity: "medium",
    time: "2025-09-18 07:55",
  },
];

export default function App() {
  const [alerts, setAlerts] = useState(initialAlerts);

  const severities = ["critical", "high", "medium", "info"];

  function addIncident() {
    const newId = alerts.length + 1;
    const severity = severities[Math.floor(Math.random() * severities.length)];
    const newAlert = {
      id: newId,
      title: `Test incident #${newId}`,
      severity,
      time: new Date().toLocaleString(),
    };
    setAlerts([newAlert, ...alerts]);
  }

  return (
    <div className="app-container">
      <header>
        <h1>Incident Dashboard</h1>
        <p className="subtitle">Real-time system alerts with severity levels</p>
        <button className="add-btn" onClick={addIncident}>
          Trigger New Incident
        </button>
      </header>

      <ul className="alerts-list">
        {alerts.map((a) => (
          <li key={a.id} className="alert-card">
            <div className="alert-header">
              <AlertBadge severity={a.severity} />
              <span className="alert-time">{a.time}</span>
            </div>
            <div className="alert-title">{a.title}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}
