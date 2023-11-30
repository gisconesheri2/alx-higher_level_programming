#!/bin/bash
# print methods allowed by te server
curl -X "OPTIONS" -sLI  "$1" | grep -i 'Allow' | awk -F' ' '{print $2, $3, $4}'
