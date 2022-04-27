#! /bin/bash

#deploy database
kubectl create namespace chatbot

kubectl create -f mysql-secret.yaml -n chatbot
kubectl create -f mysql-storage.yaml -n chatbot

kubectl create -f ../database.yaml --namespace chatbot
kubectl create -f ../database_services.yaml --namespace chatbot
