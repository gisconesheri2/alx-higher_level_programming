#!/bin/bash
# print body return if response is successful
curl -X GET -Ls --fail "$1"
