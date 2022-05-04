#!/bin/bash

kubectl exec -it $1 -n chatbot -- python cmdline_chat.py
