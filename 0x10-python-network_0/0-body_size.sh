#!/bin/bash

# The size of the response body in size bytes
url=$1
size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}')
echo"$size"

