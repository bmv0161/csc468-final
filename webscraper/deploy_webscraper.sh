#! /bin/bash

#create kubernetes registry
kubectl create deployment registry --image=registry
kubectl expose deploy/registry --port=5000 --type=NodePort
kubectl patch service registry --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":30000}]'
docker-compose build
./wait-for-it.sh 127.0.0.1:30000 -t 100 -- docker-compose push

#deploy pod
kubectl create namespace chatbot

kubectl create -f ../webscraper.yaml --namespace chatbot
kubectl create -f ../webscraper_services.yaml --namespace chatbot
