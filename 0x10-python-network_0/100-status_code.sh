#!/bin/bash
# Only status code 
curl -so $URL /dev/null -w "%{http_code}" "$1"
