#!/bin/bash
# Sends a request to a URL passed as an argument & displays the response status
curl -sI "$1" -w '%{http_code}' | tail -1
