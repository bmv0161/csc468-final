#! /bin/bash

#create kubernetes registry
kubectl create deployment registry --image=registry
kubectl expose deploy/registry --port=5000 --type=NodePort
kubectl patch service registry --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":30000}]'
docker-compose build

#launch database volumes and pod
kubectl create namespace chatbot

kubectl create -f mysql-secret.yaml -n chatbot
kubectl create -f mysql-storage.yaml -n chatbot

kubectl create -f ../database.yaml --namespace chatbot
kubectl create -f ../database_services.yaml --namespace chatbot
