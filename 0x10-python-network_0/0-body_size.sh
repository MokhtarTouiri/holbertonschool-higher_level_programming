#!/bin/bash
# cURL body size
curl -sI $URL "$1" | grep -i Content-Length | cut -d " " -f 2 

