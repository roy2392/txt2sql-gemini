#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please create .env file with your Google API key"
    exit 1
fi

# Export environment variables
export $(cat .env | xargs)

# Build and start the containers
docker-compose -f docker/docker-compose.yml up --build -d

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 10

# Show logs
docker-compose -f docker/docker-compose.yml logs -f
