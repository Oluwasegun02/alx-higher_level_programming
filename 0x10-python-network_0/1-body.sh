#!/bin/bash

URL=$1
RESPONSE=$(curl -s -w '%{http_code}' $URL)

if [[ $RESPONSE -eq 200 ]]; then
  curl -s $URL
else
  echo " $RESPONSE"
fi
