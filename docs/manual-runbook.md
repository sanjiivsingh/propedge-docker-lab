# Manual Docker Runbook

Do this before Docker Compose.

## 1. Network

```bash
docker network create propedge-network
```

## 2. Build

From each repository:

```bash
docker build -t propedge/main-dashboard:1.0 .
docker build -t propedge/backend-service:1.0 .
docker build -t propedge/trading-simulator:1.0 .
docker build -t propedge/ingestion-service:1.0 .
docker build -t propedge/database:1.0 .
```

## 3. Database

Run PostgreSQL on `propedge-network` with:

```text
POSTGRES_DB=trading
POSTGRES_USER=trader
POSTGRES_PASSWORD=traderpass
```

Container name:

```text
db
```

Later add a named volume mounted at `/var/lib/postgresql/data`.

## 4. Trading Simulator

Container name:

```text
trading-app
```

Port:

```text
5002
```

It only needs network access initially.

## 5. Ingestion

Container name:

```text
ingestion
```

Environment:

```text
DB_HOST=db
DB_NAME=trading
DB_USER=trader
DB_PASSWORD=traderpass
TRADING_URL=http://trading-app:5002
POLL_INTERVAL=3
```

## 6. Backend

Container name:

```text
backend
```

Environment:

```text
DB_HOST=db
DB_NAME=trading
DB_USER=trader
DB_PASSWORD=traderpass
```

## 7. Main Dashboard

Publish:

```text
8080:80
```

Then open:

```text
http://localhost:8080
```

Login with:

```text
trader / trader123
```

## 8. Test

Open the Trading Simulator from the main dashboard.

Generate winning/loss/random trades.

Wait a few seconds.

Return to the dashboard and refresh. The persisted trades should affect the metrics.

## 9. Inspect DNS

```bash
docker exec dashboard getent hosts backend
docker exec dashboard getent hosts trading-app
docker exec ingestion getent hosts trading-app
docker exec ingestion getent hosts db
```

## 10. Inspect the network

```bash
docker network inspect propedge-network
```

## 11. Inspect logs

```bash
docker logs dashboard
docker logs backend
docker logs trading-app
docker logs ingestion
docker logs db
```

## 12. Break it deliberately

```bash
docker stop ingestion
```

Generate trades.

The Trading Simulator keeps generating them, but they are not persisted.

Then:

```bash
docker start ingestion
```

Observe ingestion catching up.
