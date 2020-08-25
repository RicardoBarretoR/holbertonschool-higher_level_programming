#!/usr/bin/python3
""" 
sends a request to the URL and Show
the value of x-Request-Id variable

"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        meta = response.info()
        for header in meta._headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
