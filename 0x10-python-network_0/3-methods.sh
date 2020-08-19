#!/bin/bash
#Take a URL and show all the HTTP methods
curl -sL "$1" | grep "Allow" | cut -d " " -f 2-
