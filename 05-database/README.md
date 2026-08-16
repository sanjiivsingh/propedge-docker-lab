# PropEdge Database

## Purpose
PostgreSQL persistence layer.

Stores:
- `users`
- `account`
- `ingested_trades`

## Runtime
- PostgreSQL 16
- Container port: `5432`

## Initialization
The SQL initialization file must be copied into:

```text
/docker-entrypoint-initdb.d/
```

It runs when PostgreSQL initializes a new data directory.

## Runtime environment

```text
POSTGRES_DB=trading
POSTGRES_USER=trader
POSTGRES_PASSWORD=traderpass
```

## Seed data

```text
username: trader
password: trader123

account: DEMO-50000
starting balance: 50000
```

The password is deliberately plain text for this educational lab. Do not use this authentication design in production.

## Persistence
Use a Docker named volume mounted at:

```text
/var/lib/postgresql/data
```

## Dockerfile reconstruction challenge
Delete `Dockerfile` after initial testing.

From this README and `init.sql`, determine:
- PostgreSQL base image/version
- initialization directory
- SQL file to copy
- container port
- required runtime environment variables
- persistence directory

The final Dockerfile should be very small because the PostgreSQL image already supplies the database server and startup logic.
