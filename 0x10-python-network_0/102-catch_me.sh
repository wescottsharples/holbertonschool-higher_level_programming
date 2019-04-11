#!/bin/bash
# Bash script gets hidden message using curl
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
