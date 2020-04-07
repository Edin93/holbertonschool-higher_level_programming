#!/bin/bash
# Requests to 0.0.0.0:5000/catch_me that causes the server to respond.
curl -L  0.0.0.0:5000/catch_me -X PUT -d user_id="98"
