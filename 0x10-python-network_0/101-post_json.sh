#!/bin/bash
# post data to the server using json
curl --data @"$2" --header "Content-Type: application/json" --header "Accept: application/json" --request "POST" -sL  "$1"
