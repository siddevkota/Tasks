# Task 4

Basic Data Pipeline Automation - Task: Script Data Extraction Problem: Write a simple script to extract data from the chosen source. Expected Outcome: Script that outputs raw data to a file. Tools: Python, shell script. Research: File I/O, database queries. Consider: Error handling, efficiency.

This is a Python script for extracting and processing airline data SQLite database.
Used SQLite db from https://www.kaggle.com/datasets/saadharoon27/airlines-dataset

## Quick Start

1. **Run the extraction script:**
   ```bash
   python extract_airlines.py
   ```

## Files

- `extract_airlines.py` - Main data extraction script
- `flights.csv` - Flight data in CSV format extracted
- `travel.sqlite` - SQLite database with travel data

## Requirements

- Python 3.x
- sqlite3 (built-in)
- pandas (if used in script)

## Usage

```bash
python extract_airlines.py
```

The script processes flight data from both CSV and SQLite sources to extract airline information.
