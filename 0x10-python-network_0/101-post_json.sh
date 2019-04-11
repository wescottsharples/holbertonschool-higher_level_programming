#!/bin/bash
# Script sends JSON request to URL
curl -sd @"$2" "$1" -H "Content-Type: application/json"
