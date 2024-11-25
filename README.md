# Natural Language to SQL Query API
A FastAPI application that converts natural language questions to SQL queries using Google’s Gemini LLM, executes them on a PostgreSQL database, and returns both the results and a natural language explanation.
## Features
	•	Natural language to SQL conversion using Google Gemini LLM
	•	PostgreSQL database integration
	•	RESTful API endpoints
	•	Docker containerization
	•	Automated database initialization
	•	Health monitoring
	•	Comprehensive test suite
## Architecture Overview
    ```mermaid
    graph LR
    A[Client Request] --> B[FastAPI Endpoint]
    B --> C[SQL Generator]
    C --> D[Gemini LLM]
    D --> C
    C --> E[Database Manager]
    E --> F[PostgreSQL]
    F --> E
    E --> B
    B --> G[Natural Language Response]
    G --> H[Client Response]
    ```
## Prerequisites
	•	Docker and Docker Compose
	•	Google Cloud API key for Gemini LLM
	•	Git
## Quick Start
	1.	Clone the repository:
    ```bash
git clone <repository-url>
cd <repository-name>
```
    2.	Create a `.env` file in the root directory with the following environment variables:
    ```bash
   cp .env.example .env
```
    3.	Add your Google API key to `.env`:
    ```bash
GOOGLE_API_KEY=your_key_here
```
    4. Run the application:
    ```bash
./run.sh
```
The API will be available at `http://localhost:8000`.

## API Endpoints

### Health Check:
```bash
GET /health
```

### Query Endpoint
```bash
POST /query
Content-Type: application/json

{
    "question": "What is the average age of users?"
}
```
### Example response:
```bash
{
    "query": "SELECT AVG(age) FROM users",
    "result": [
        {
            "avg": 30
        }
    ],
    "explanation": "The average age of users is 30."
}
```

## Development
Running Tests
```bash
pytest tests/
```

Modifying Database Schema
    1.	Update `docker/init.sql`
	2.	Update `src/utils/sql_generator.py` schema
	3.	Rebuild containers:
    ```bash
docker-compose -f docker/docker-compose.yml up --build -d
```