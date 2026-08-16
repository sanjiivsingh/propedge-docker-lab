# PropEdge Main Dashboard

## Purpose
Trader-facing web portal with login, account metrics, recent trades, equity curve, and a link to the separate Trading Simulator.

## Runtime
- Nginx
- Container port: `80`
- Host port in lab: `8080`

## Reverse proxy
Nginx must route:

```text
/api/       -> backend:5000
/trading/   -> trading-app:5002
```

Use Docker service names, not IP addresses.

## Dockerfile reconstruction challenge
After initial testing, delete `Dockerfile`.

From this README and the source, determine:
- appropriate Nginx base image
- static document root
- configuration path
- files to copy
- port
- startup behavior

Build context is this repository.

## Expected result
The rebuilt image serves the dashboard on port 80 and proxies both application paths correctly.
