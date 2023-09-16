
#!/bin/sh
docker compose --profile main-service up --build -d
sleep 20
docker compose --profile app up --build -d