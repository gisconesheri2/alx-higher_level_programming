#!/bin/bash
# add additioninfo on the header
curl --header "X-School-User-Id: 98" --request "GET" -sL  "$1"
