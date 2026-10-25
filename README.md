<div align="center">

# ⚡ PropEdge Trading Platform Lab

### High-Concurrency Containerized Proprietary Trading System Architecture

<p align="center">
  <img src="https://img.shields.io/badge/Container-Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose" />
  <img src="https://img.shields.io/badge/Backend-Python_FastAPI%2FFlask-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL_16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Proxy-Nginx_Alpine-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx" />
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="CI/CD" />
</p>

</div>

---

## 📌 Executive Overview

**PropEdge** is a multi-tier containerized simulated proprietary trading platform engineered to demonstrate:
- **Segregated Docker Bridge Networks:** Independent internal network tiers preventing direct external access to databases and ingestion engines.
- **Service-to-Service DNS Resolution:** Container orchestration without hardcoded IP dependencies.
- **High-Frequency Ingestion & State Persistence:** Automated trade ingestion pipeline feeding a transactional PostgreSQL database with named volume persistence.
- **Reverse Proxy Architecture:** Nginx edge proxy directing client traffic to frontend dashboards and authenticated backend APIs.
- **Cloudflare Tunnel Ingress Ready:** Hardened zero-trust edge ingress avoiding open incoming firewall ports.

---

## 🏗️ Multi-Tier Architecture & Network Isolation

```mermaid
flowchart TD
    Client["🌐 Trader Browser"] -->|Port 8080| Dashboard["🖥️ Nginx Main Dashboard\n(propedge-dashboard)"]

    subgraph FrontendNet["🌐 frontend-net (Bridge)"]
        Dashboard -->|Proxy /api| Backend["⚙️ Backend Service\n(propedge-backend:5000)"]
    end

    subgraph BackendNet["🔄 backend-net (Bridge)"]
        Simulator["📈 Trading Simulator\n(propedge-trading-simulator:5002)"]
        Ingestion["⚡ Ingestion Service\n(propedge-ingestion:5001)"]
        Ingestion -->|Polls Order Book| Simulator
    end

    subgraph DataNet["🔒 data-net (Bridge - Isolated)"]
        Backend -->|Query Trade Data| DB[("🗄️ PostgreSQL 16 DB\n(propedge-db:5432)")]
        Ingestion -->|Insert Transactions| DB
    end

    classDef pub fill:#0b1329,stroke:#38bdf8,stroke-width:1.5px,color:#fff;
    classDef mid fill:#14213d,stroke:#818cf8,stroke-width:1.5px,color:#fff;
    classDef secure fill:#052e16,stroke:#10b981,stroke-width:1.5px,color:#fff;
    class Dashboard pub;
    class Backend,Simulator,Ingestion mid;
    class DB secure;
```

---

## 🧰 Microservice Architecture

| Service Directory | Container Name | Stack & Runtime | Internal Port | Network Attachments | Responsibility |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `01-main-dashboard` | `propedge-dashboard` | Nginx Alpine | `80` (Host `8080`) | `frontend-net` | Trader portal UI, static assets, reverse proxy |
| `02-backend-service` | `propedge-backend` | Python 3.12, psycopg2 | `5000` | `frontend-net`, `data-net` | Authentication, REST API endpoints, business logic |
| `03-trading-simulator` | `propedge-trading-simulator` | Python 3.12 | `5002` (Host `5002`) | `backend-net`, `data-net` | Market simulation engine, randomized order book |
| `04-ingestion-service` | `propedge-ingestion` | Python 3.12 | `5001` | `backend-net`, `data-net` | Polling worker ingesting simulated trades into DB |
| `05-database` | `propedge-db` | PostgreSQL 16 Alpine | `5432` | `data-net` | Schema migrations, transaction seed data, named volume |

---

## 🚀 Quickstart & Orchestration

### 1. Launch Complete Stack

```bash
# Clone and spin up all microservices with parallel build
git clone https://github.com/sanjiivsingh/PropEdge-Docker-Lab.git
cd PropEdge-Docker-Lab

docker compose -f compose.yaml up -d --build
```

### 2. Verify Service Health

```bash
# Check container status and healthchecks
docker compose -f compose.yaml ps

# Inspect live ingestion logs
docker compose -f compose.yaml logs -f ingestion
```

### 3. Access Trader Portal

* **Trader Dashboard:** Open `http://localhost:8080`
* **Demo Credentials:**
  ```text
  Username: trader
  Password: trader123
  ```
* **Simulator Direct API:** `http://localhost:5002`

---

## 🛡️ Security & Zero-Trust Best Practices

1. **Network Demarcation:** The `propedge-db` database is exclusively connected to `data-net`. It exposes **zero ports** to the host machine or public internet.
2. **Health Check Orchestration:** Backend and Ingestion services utilize `condition: service_healthy` depending on PostgreSQL's `pg_isready` probe before starting.
3. **Graceful Degradation:** All services run with automatic container restarts (`restart: unless-stopped`).
4. **Volume Persistence:** Data is retained safely across container updates in named volume `postgres_data`.

---

## 📄 License

MIT License - open for educational and enterprise architectural demonstration.
