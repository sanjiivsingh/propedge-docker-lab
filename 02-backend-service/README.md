# PropEdge Backend Service

## Purpose
Flask API for authentication, dashboard data, and business calculations.

## Runtime
- Python 3
- Flask
- psycopg2
- Container port: `5000`

## Dependencies
See `requirements.txt`.

## Environment variables

```text
DB_HOST=db
DB_NAME=trading
DB_USER=trader
DB_PASSWORD=traderpass
```

## Endpoints

```text
GET  /health
POST /api/login
GET  /api/dashboard
```

## Database requirements
The database must contain:

```text
users
account
ingested_trades
```

## Business rules
Starting balance: `$50,000`

Daily loss limit: `$1,000`

Maximum drawdown: `$2,500`

The account becomes `FAILED` if either limit is breached.

## Dockerfile reconstruction challenge
Delete `Dockerfile` after initial testing. Determine the Python base image, working directory, dependency installation, source files, port, environment variables, and startup command from this README and the source.
