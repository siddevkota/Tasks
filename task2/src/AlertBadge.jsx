import React from "react";

const styles = {
  critical: { background: "#b71c1c", color: "white" },
  high: { background: "#e65100", color: "white" },
  medium: { background: "#fbc02d", color: "black" },
  info: { background: "#1976d2", color: "white" },
};

export default function AlertBadge({ severity }) {
  const style = {
    ...styles[severity],
    padding: "0.3rem 0.6rem",
    borderRadius: "999px",
    fontSize: "0.8rem",
    fontWeight: "600",
    textTransform: "capitalize",
    boxShadow: "0 2px 6px rgba(0,0,0,0.15)",
  };

  return <span style={style}>{severity}</span>;
}
