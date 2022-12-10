#!/bin/bash
pwd
cd "ingress"
echo "Starting ingress.."
kubectl apply -f ingress.yml
cd ..
cd "frontend"
echo "Starting frontend.."
kubectl apply -f nginx.yml
kubectl apply -f service.yml
cd ..
cd "api"
echo "Starting API.."
kubectl apply -f api.yml
kubectl apply -f api-service.yml
cd ..
cd "database"
echo "Starting database.."
kubectl apply -f database.yml
kubectl apply -f db_service.yml