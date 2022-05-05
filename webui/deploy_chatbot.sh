#! /bin/bash

#kubectl create deployment registry --image=registry
#kubectl expose deploy/registry --port=5000 --type=NodePort
#kubectl patch service registry --type='json' --patch='[{"op": "replace", "path": "/spec/ports/0/nodePort", "value":35000}]'

docker-compose build
./wait-for-it.sh 127.0.0.1:35000 -t 15 -- docker-compose push

#kubectl create namespace chatbot

kubectl create -f ../webui.yaml --namespace chatbot
kubectl create -f ../webui_services.yaml --namespace chatbot
