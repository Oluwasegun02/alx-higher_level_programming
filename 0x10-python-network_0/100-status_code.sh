#!/bin/bash

if [ $# -eq 0 ]
then
  echo "Usage: $0 URL"
  exit 1
fi

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
echo "$response"

