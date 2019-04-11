#!/bin/bash
# Sends a POST request and displays response of given URL
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
