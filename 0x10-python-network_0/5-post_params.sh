#!/bin/bash
#A URL, send a POST request and display the body of the response
curl -s --data "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
