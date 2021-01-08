#!/bin/bash
# sends a JSON POST request to a URL passed 
curl -s $URL -X POST -d @"$2" -H Content-Type: application/json "$1"
