# Customer Data Pipeline

An end-to-end data pipeline built with:

- **Flask** — Mock customer data API  
- **FastAPI** — Data ingestion & query service  
- **PostgreSQL** — Data storage  
- **Docker & Docker Compose** — Containerization & orchestration  

---

## Overview

This project demonstrates a simple microservices-based data pipeline:

Flask API (Mock Data)  
↓  
FastAPI (Ingestion Service)  
↓  
PostgreSQL (Database)  
↓  
API Response  

---

## Project Structure

customer-data-pipeline/  
│  
├── docker-compose.yml  
├── README.md  
│  
├── flask-mock-server/  
│   ├── app/  
│   ├── data/  
│   ├── Dockerfile  
│   ├── requirements.txt  
│   └── run.py  
│  
└── pipeline-service/  
    ├── main.py  
    ├── database.py  
    ├── models/  
    ├── services/  
    ├── Dockerfile  
    └── requirements.txt  

---

## Prerequisites

Make sure you have installed:

- Docker  
- Docker Compose  

---

## How to Run

### 1. Clone the repository

git clone <repo-url>  
cd customer-data-pipeline  

---

### 2. Run all services

docker-compose up --build  

This command will:
- Build all Docker images (Flask + FastAPI)
- Start PostgreSQL
- Connect all services automatically

---

## Services

| Service          | URL                    |
|------------------|------------------------|
| Flask Mock API   | http://localhost:5000 |
| FastAPI Service  | http://localhost:8000 |
| PostgreSQL       | localhost:5432        |

---

## API Usage

### Ingest Data

POST /api/ingest  

Response:
{
  "status": "success",
  "records_processed": 20
}

---

### Get Customers

GET /api/customers?page=1&limit=10  

---

### Get Customer by ID

GET /api/customers/{customer_id}  

---

## Key Features

- JSON-based mock data source (Flask)  
- Automated ingestion with pagination  
- Upsert logic (insert/update)  
- PostgreSQL persistence  
- Microservices architecture  
- Fully Dockerized  

---

## Notes

- No need to manually run docker build  
- docker-compose handles everything  
- Services communicate via Docker network  

---

## Author

Vincent Joel Sinatra