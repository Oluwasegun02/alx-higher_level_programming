#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    data_res = requests.get(url, auth=(user, passwd))

    if data_res.status_code == 200:
        user_data = data_res.json()
        print(f"{user_data['id']}")
    else:
        print(f"{data_res.status_code}")
