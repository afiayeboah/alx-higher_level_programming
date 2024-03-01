#!/usr/bin/python3
"""
Python script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
