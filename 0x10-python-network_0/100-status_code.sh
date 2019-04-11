#!/bin/bash
# Displays status code of given URL
curl -o /dev/null -sw '%{http_code}' "$1"
