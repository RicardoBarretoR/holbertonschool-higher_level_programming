#!/bin/bash
#Send DELETED request as first argument and show body of answer
curl -sX DELETE "$1"
