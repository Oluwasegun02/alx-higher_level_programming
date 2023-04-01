#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
  the URL, and displays the value of the X-Request-Id variable found 
  in the header of the response using the requests package
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    m = requests.get(url)
    x_request_id = m.headers.get("X-Request-Id")
    print(x_request_id)
