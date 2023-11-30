#!/bin/bash
# post data to the server
curl --data "email=test@gmail.com" --data "subject=I will always be here for PLD" --request "POST" -sL  "$1"
