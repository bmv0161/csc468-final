kubectl delete all --all -n chatbot
kubectl delete pvc --all -n chatbot
kubectl delete pv mysql-pv -n chatbot
kubectl delete sc mysql-sc -n chatbot
kubectl delete namespace chatbot
#kubectl delete svc registry
#kubectl delete deployment registry
