# Docker Compose Exercise

Create this only after the five manual Dockerfiles have been reconstructed and tested.

Create:

```text
compose.yaml
```

at the root.

Services:

```text
dashboard
backend
trading-app
ingestion
db
```

Compose must:
- build all five repositories
- create the shared network
- use service names for DNS
- pass environment variables
- publish the Main Dashboard
- persist PostgreSQL with a named volume
- express startup dependencies
- support `docker compose up --build`

Do not mechanically copy every `docker run` flag. Decide whether each setting belongs to the image, container runtime, network, persistence, or application configuration.
