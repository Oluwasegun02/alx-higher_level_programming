#!/bin/bash
url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST "$url" \
     -d "email=$email" \
     -d "subject=$subject" \
     -o response.txt

