import sqlite3
import csv
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

DB_FILE = Path("travel.sqlite")
OUTPUT_FILE = Path("flights.csv")


def extract_data(query: str, output: Path):
    try:
        logging.info(f"Connecting to {DB_FILE}")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        logging.info(f"Running query: {query}")
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]

        logging.info(f"Writing {len(rows)} rows to {output}")
        with output.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        logging.info("Extraction complete.")
        return True
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        return False
    finally:
        if "conn" in locals():
            conn.close()


if __name__ == "__main__":
    query = "SELECT flight_id, departure_airport, arrival_airport, scheduled_departure, scheduled_arrival FROM flights LIMIT 50;"
    extract_data(query, OUTPUT_FILE)
