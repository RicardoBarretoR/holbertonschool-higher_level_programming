#!/bin/bash
#A URL, send a POST request and display the body of the response
#variable email must be sent with the value hr@holbertonschool.com
#variable subject must be sent with the value I will always be here for PLD
curl -s -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
