# KyraWorks Tasks Collection

A collection of development tasks covering React components, data processing, and containerized applications.

## 📋 Task Overview

| Task                                                        | Description                           | Technology Stack            |
| ----------------------------------------------------------- | ------------------------------------- | --------------------------- |
| [Task 1](./task1/BasicLogAggregationStrategy-Task1.pdf)     | Define Basic Log Aggregation Strategy | PDF                         |
| [Task 2](./task2)                                           | Display Severity in UI                | React, Vite, ESLint         |
| [Task 3](./task3)                                           | Handle Sync Errors                    | Python                      |
| [Task 4](./task4)                                           | Script Data Extraction                | Python, SQLite, CSV         |
| [Task 5](./task5/IncidentResponsePlaybook-Task5.pdf)        | Outline Manual Response Steps         | PDF                         |
| [Task 6](./task6/UsageAnalyticsforVideoStreaming-Task6.pdf) | Define Usage Analytics Goals          | PDF                         |
| [Task 7](./task7)                                           | Deploy Core Services                  | FastAPI, PostgreSQL, Docker |
| [Task 8](./task8)                                           | Create Content Template Bank          | PDF, Canva                  |

## 🚀 Quick Start

### Task 2 - React Alert Badge

```bash
cd task2
npm install
npm run dev
```

Access: http://localhost:5173

### Task 3 - Data Sync

```bash
cd task3
python sync.py
```

### Task 4 - Airlines Data

```bash
cd task4
python extract_airlines.py
```

### Task 7 - Dockerized API

```bash
cd task7
docker-compose up --build
```

Access: http://localhost:8000

## 🛠️ Technologies Used

- **Frontend**: React 18, Vite
- **Backend**: FastAPI, Python
- **Database**: PostgreSQL, SQLite
- **DevOps**: Docker, Docker Compose
- **Data**: CSV processing, JSON output

## 📁 Project Structure

```
KyraWorks-Tasks/
├── task2/          # React Alert Badge Component
├── task3/          # Data Sync Utility
├── task4/          # Airlines Data Extraction
├── task7/          # Dockerized FastAPI Application
└── README.md       # This file
```

## 🔧 Prerequisites

- **Node.js** 14.18+ (for Task 2)
- **Python** 3.x (for Tasks 3, 4, 7)
- **Docker & Docker Compose** (for Task 7)

## 📊 Task Details

### Task 2:

- Build model warm-up and fallback mechanisms:
  - Task: Display Severity in UI
  - Problem: Update the UI to clearly show the severity level of each alert/incident.
  - Expected Outcome: UI elements displaying alert severity.
  - Tools: Frontend framework.
  - Research: UI design.
  - Consider: Visual cues, accessibility.

### Task 3:

- Build synthetic data generation for edge cases
  - Task: Handle Sync Errors
  - Problem: Add error handling/logging for cases where synchronization fails or is poor.
  - Expected Outcome: Errors logged, potential fallback behavior.
  - Tools: Code editor, logging.
  - Research: Error handling.
  - Consider: Alerting, data integrity.

### Task 4:

- Basic Data Pipeline Automation
  - Task: Script Data Extraction
  - Problem: Write a simple script to extract data from the chosen source.
  - Expected Outcome: Script that outputs raw data to a file.
  - Tools: Python, shell script.
  - Research: File I/O, database queries.
  - Consider: Error handling, efficiency.

### Task 7:

- Create model versioning and A/B testing framework
  - Task: Deploy Core Services
  - Problem: Deploy essential services (e.g., database, API) to the primary region.
  - Expected Outcome: Core services running in primary region.
  - Tools: Deployment tools, cloud console.
  - Research: Service deployment.
  - Consider: Configuration, secrets.

## 🏃‍♂️ Running All Tasks

Each task can be run independently. See individual task README files for detailed instructions.
