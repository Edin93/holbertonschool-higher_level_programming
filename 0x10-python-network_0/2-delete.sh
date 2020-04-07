#!/bin/bash
# Send a DELETE request to the URL(arg1) and displays the body of the response.
curl -s "$1" -X DELETE
