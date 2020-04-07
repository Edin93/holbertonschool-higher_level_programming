#!/bin/bash
# Sends a JSON POST request to a URL (arg 1), and displays the response body.
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
