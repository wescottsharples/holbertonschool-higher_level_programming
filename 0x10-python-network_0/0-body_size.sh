#!/usr/bin/env bash
# Curls the body size

curl -sI "$1" | grep Content-Length | cut -f 2 -d ':'
