#!/usr/bin/python3
"""
Python script that sends a POST request with an email parameter
to a given URL and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)
