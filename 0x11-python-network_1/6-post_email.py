#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.

"""
if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
