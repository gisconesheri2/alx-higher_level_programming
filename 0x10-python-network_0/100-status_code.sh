#!/bin/bash
# displays status code of server
curl -o /dev/nul -s --location --head  --write-out "%{http_code}" "$1"
