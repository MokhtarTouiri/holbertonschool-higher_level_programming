#!/bin/bash
# cURL only methods
curl -sI $URL "$1" | grep -i "Allow" | cut -c 8-
