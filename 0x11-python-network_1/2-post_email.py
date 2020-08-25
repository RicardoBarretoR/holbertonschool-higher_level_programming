#!/usr/bin/python3
"""
displays the body of the response (decoded in utf-8)

"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    parameters = {'email': email}

    data = urllib.parse.urlencode(parameters)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
