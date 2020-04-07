#!/bin/bash
# takes in a URL(arg), sends a GET request to it & display the body of the rep.
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
