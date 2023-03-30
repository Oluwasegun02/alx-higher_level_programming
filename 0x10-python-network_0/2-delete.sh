#!/bin/bash
#Bash script that sends a DELETE request to the URL passed
if [ $# -eq 0 ]; then
  echo "Please provide a URL as an argument"
  exit 1
fi

url="$1"

response=$(curl -sSL -X DELETE "$url")
status_code=$(echo "$response" | head -n 1 | awk '{print $2}')

if [ "$status_code" -ne 200 ]; then
  echo "$status_code"
else
  echo "$response"
fi
