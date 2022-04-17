#! /bin/bash

kubectl create deployment registry --image=registry
kubectl expose deploy/registry --port=5555 --type=NodePort
kubectl patch service registry --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":30000}]'

docker-compose build
docker-compose push

kubectl create namespace chatbot

kubectl apply -f database/mysql-secret.yaml -n chatbot
kubectl apply -f database/mysql-storage.yaml -n chatbot

kubectl create -f chatbot-deployment.yaml --namespace chatbot
kubectl create -f chatbot-services.yaml --namespace chatbot
