# Task 7

Create model versioning and A/B testing framework - Task: Deploy Core Services Problem: Deploy essential services (e.g., database, API) to the primary region. Expected Outcome: Core services running in primary region. Tools: Deployment tools, cloud console. Research: Service deployment. Consider: Configuration, secrets.

This is code for a containerized FastAPI application with PostgreSQL database for model version management. It is to demonstrate a dummy application deployment.

## Quick Start

1. **Build and run the application:**

   ```bash
   docker-compose up --build
   ```

2. **Access the application:**

   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

## Services

- **API**: FastAPI application (port 8000)
- **Database**: PostgreSQL database (port 5432)

## Project Structure

```
task7/
├── docker-compose.yml    # Service orchestration
├── api/
│   ├── app.py           # FastAPI application
│   ├── Dockerfile       # API container config
│   └── requirements.txt # Python dependencies
└── db/
    └── init.sql         # Database initialization
```

## API Endpoints

- `GET /` - Health check
- `GET /versions` - Get model versions

## Requirements

- Docker
- Docker Compose

## Development

Run in detached mode:

```bash
docker-compose up -d --build
```

View logs:

```bash
docker-compose logs api
docker-compose logs db
```

## Technologies

- FastAPI
- PostgreSQL
- Docker
- Docker Compose
