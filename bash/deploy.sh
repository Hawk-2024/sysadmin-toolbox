#!/bin/bash
echo "Deploying Flask app..."
docker-compose -f ../docker/docker-compose.yml up -d --build
