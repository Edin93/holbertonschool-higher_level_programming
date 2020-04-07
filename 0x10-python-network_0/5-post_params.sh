#!/bin/bash
# takes in a URL, sends a POST request to it, and displays the response body.
curl -s -X POST -d email="hr@holbertonschool.com" -d subject="I will always be here for PLD" "$1"
