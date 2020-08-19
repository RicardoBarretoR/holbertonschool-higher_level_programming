#!/bin/bash
#Take a URL and show all the HTTP methods
curl -sI $1 | grep Allow | cut -f2- -d' '
