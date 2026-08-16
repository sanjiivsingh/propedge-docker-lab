# PropEdge Trading Simulator

## Purpose
Separate data-producing application.

It generates:
- random trades
- winning trades
- losing trades

It does NOT connect to PostgreSQL.

## Runtime
- Python 3
- Flask
- Container port: `5002`

## Endpoints

```text
GET  /
GET  /api/trades?after_id=N
POST /api/generate/random
POST /api/generate/win
POST /api/generate/loss
```

## Behavior
Trades are held in application memory. Restarting this container clears the simulator's generated trades.

## Dockerfile reconstruction challenge
Delete `Dockerfile` after initial testing. Determine the Python base image, dependency installation, working directory, required source/HTML files, port, and startup command from this README and the source.

## Expected network access
The ingestion service must be able to call:

```text
http://trading-app:5002/api/trades
```
