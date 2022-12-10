#!/bin/bash
echo "Removing all deployments & services & ingress"
kubectl delete deployment api-deployment-bv
kubectl delete deployment database-deployment-bv
kubectl delete deployment nginx-deployment-bv
kubectl delete service api-service-bv
kubectl delete service db-service-bv
kubectl delete service nginx-service-bv
kubectl delete ingress nginx-ingress-bv