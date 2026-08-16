# Dockerfile Rebuild Challenge

After the complete supplied solution works, delete every `Dockerfile`.

Do not recreate them from memory or copy them from another repository.

For each repository, read its README and inspect its source.

## Main Dashboard
Determine:
- Nginx base image family
- static document root
- Nginx configuration location
- required files
- port
- startup behavior

## Backend
Determine:
- Python base image
- dependency installation
- working directory
- source file
- port
- startup command
- database environment variables

## Trading Simulator
Determine:
- Python base image
- Flask dependency
- source and HTML files
- port
- startup command

## Ingestion
Determine:
- Python base image
- Flask, requests, psycopg2 dependencies
- source file
- port
- environment variables
- startup command

## Database
Determine:
- PostgreSQL image/version
- initialization directory
- SQL file location
- port
- PostgreSQL environment variables
- persistence directory

Build and test each image independently before moving to Compose.
