#!/bin/bash
# cURL body size
curl --compressed -so /dev/null "1$" -w '%{size_download}\n'
