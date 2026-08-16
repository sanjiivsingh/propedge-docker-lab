# PropEdge Docker Lab

A small prop-trading platform for learning Docker, networking, DNS, service-to-service HTTP, persistence, reverse proxies, and Docker Compose.

## Architecture

Browser -> Main Dashboard -> Backend -> PostgreSQL
                         \
                          -> Trading Simulator
Ingestion Service -> Trading Simulator
Ingestion Service -> PostgreSQL

## Repositories

| Repository | Responsibility |
|---|---|
| `propedge-main-dashboard` | Main trader portal, login UI, Nginx reverse proxy |
| `propedge-backend-service` | Authentication, dashboard API, business logic |
| `propedge-trading-simulator` | Separate application that generates trades |
| `propedge-ingestion-service` | Fetches simulator trades and stores them |
| `propedge-database` | PostgreSQL schema and seed data |

## Demo credentials

```text
Username: trader
Password: trader123
```

Authentication is deliberately educational, not production security.

## Learning sequence

### Phase 1 - Run the supplied solution
Build the supplied Dockerfiles, create one Docker network, run all five containers manually, inspect DNS/IPs/logs, and prove the complete data flow.

### Phase 2 - Rebuild the Dockerfiles yourself
After the application works, DELETE every supplied Dockerfile.

For each repository:
1. Read its README.
2. Inspect the source files.
3. Identify runtime, dependencies, entry point, required files, port, environment variables, and startup command.
4. Write the Dockerfile yourself.
5. Build and test it.
6. Do not use Docker Compose yet.

The READMEs document requirements but intentionally do not give the Dockerfile solution.

### Phase 3 - Docker Compose
After all five Dockerfiles work again, create a root `compose.yaml` and replace the manual `docker network`/`docker run` workflow.

Do not add Kubernetes, Redis, Kafka, real market APIs, JWT/OAuth, or cloud infrastructure yet.
