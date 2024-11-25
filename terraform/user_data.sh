#!/bin/bash

# Update system and install Docker
apt-get update -y
apt-get install docker.io -y
systemctl start docker
systemctl enable docker

# Install Docker Compose
apt-get install zip unzip -y
docker-compose version || (
  echo "Installing Docker Compose..."
  curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
)

# Clone the repository (replace with your repo URL)
git clone https://github.com/roy2392/txt2sql-gemini.git /app
cd /app

# Run Docker Compose
docker-compose up -d
