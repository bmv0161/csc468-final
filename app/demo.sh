#!/bin/bash

kubectl exec -it $1 chatbot-rasa -n chatbot -- python cmdline_chat.py
