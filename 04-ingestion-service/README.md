# PropEdge Ingestion Service

## Purpose
Integration service between the Trading Simulator and PostgreSQL.

It polls the simulator, fetches trades newer than the highest stored source ID, and inserts them into PostgreSQL.

## Runtime
- Python 3
- Flask
- requests
- psycopg2
- Container port: `5001`

## Environment variables

```text
DB_HOST=db
DB_NAME=trading
DB_USER=trader
DB_PASSWORD=traderpass
TRADING_URL=http://trading-app:5002
POLL_INTERVAL=3
```

## Endpoints

```text
GET  /health
POST /sync
```

## Polling
The application starts a background loop. Every `POLL_INTERVAL` seconds it:
1. reads the highest persisted `source_id`
2. requests newer trades from the simulator
3. inserts new trades
4. commits
5. repeats

Temporary failures should be logged and retried.

## Idempotency
`source_id` is the primary key. Inserts use conflict handling so the same source trade is not stored twice.

## Dockerfile reconstruction challenge
Delete `Dockerfile` after initial testing. Determine the Python base image, dependency installation, working directory, source files, port, environment variables, and startup command.

The service must reach:

```text
http://trading-app:5002
db:5432
```
