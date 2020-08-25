#!/usr/bin/python3
""" python script that fetches a web

"""
import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        content = body.decode('utf-8')
        print_str = '''Body response:
    \t- type:{}
    \t- content:{}
    \t- utf8 content: {}'''.format(type(body), body, content)
        print(print_str)
