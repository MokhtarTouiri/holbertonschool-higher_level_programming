#!/bin/bash
# cURL post parameters
curl -s $URL "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
