# PropEdge Architecture

## Components

### Main Dashboard
Nginx + HTML/CSS/JavaScript. Browser-facing application and reverse proxy.

```text
/api/*     -> backend:5000
/trading/* -> trading-app:5002
```

### Backend
Flask API. Verifies the demo user, reads PostgreSQL, calculates account metrics, and returns JSON.

### Trading Simulator
Separate Flask application. Generates random/winning/losing trades and exposes them through HTTP. It does not connect to PostgreSQL.

### Ingestion
Flask/Python integration service. Polls the Trading Simulator for new trade IDs and inserts new trades into PostgreSQL.

### Database
PostgreSQL stores users, account data, and ingested trades.

## Docker networking

All services share a user-defined bridge network.

Expected DNS names:

```text
dashboard
backend
trading-app
ingestion
db
```

Use service names, never hardcoded container IPs.

Examples:

```text
http://trading-app:5002/api/trades
db:5432
backend:5000
```

## Data ownership

Trading Simulator = generated source data.

Ingestion = transfer/integration.

PostgreSQL = persisted data.

Backend = business calculations.

Dashboard = presentation.
