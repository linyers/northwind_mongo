#/usr/bin/bash

MONGO_HOST="127.0.0.1"
MONGO_PORT="27017"
MONGO_USERNAME="admin"
MONGO_PASSWORD="123456"
AUTH_DB="admin"
DB_NAME="Northwind"
JSON_DIR="/northwind_json"

echo "Creating Northwind database..."

for JSON_FILE in $JSON_DIR/*.json; do
  COLLECTION_NAME=$(basename "$JSON_FILE" .json)
  echo "Creating collection: $COLLECTION_NAME"
  mongoimport --host $MONGO_HOST --port $MONGO_PORT \
              --username $MONGO_USERNAME --password $MONGO_PASSWORD \
              --authenticationDatabase $AUTH_DB \
              --db $DB_NAME --collection $COLLECTION_NAME \
              --file $JSON_FILE --jsonArray
done
