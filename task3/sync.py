# sync.py
import json
import logging
import random
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

OUTPUT_FILE = Path("output.json")


def fetch_data():
    """
    Mock function.
    It randomly fails to mimic sync errors.
    """
    if random.random() < 0.3:
        raise ConnectionError("Network error while fetching data")
    return {"id": int(time.time()), "value": "sample data"}


def store_data(data: dict):
    """
    Mock function to store data.
    """
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logging.info(f"Data stored in {OUTPUT_FILE}")


def sync_with_retry(max_retries: int = 3) -> bool:
    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Attempt {attempt} to sync...")
            data = fetch_data()
            store_data(data)
            logging.info("[DONE] Sync completed successfully.")
            return True
        except Exception as e:
            logging.error(f"[NOT DONE] Error during sync: {e}")
            if attempt < max_retries:
                logging.warning("Retrying...")
                time.sleep(1)
            else:
                logging.critical("Max retries reached. Falling back...")
                fallback_data = {"fallback": True, "timestamp": time.ctime()}
                store_data(fallback_data)
                return False
    return False


if __name__ == "__main__":
    success = sync_with_retry(3)
    if success:
        print("Sync finished successfully.")
    else:
        print("Sync failed. Fallback data written.")
