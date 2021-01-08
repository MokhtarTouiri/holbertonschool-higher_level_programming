#!/bin/bash
# cURL body size
curl -s "$1" -I $URL | grep -i Content-Length | cut -d " " -f 2 

