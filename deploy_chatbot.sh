#! /bin/bash

kubectl create deployment registy --image=registry
kubectel expose deploy/registry --port=30000 --type=NodePort

docker-compose build
docker-compose push

kubectl create namespace chatbot

kubectl apply -f database/mysql-secret.yaml -n chatbot
kubectl apply -f database/mysql-pv.yaml -n chatbot

kubectl create -f chatbot-deployment.yaml --namespace chatbot
kubectl create -f chatbot-services.yaml --namespace chatbot
