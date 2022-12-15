#!/usr/bin/env bash
# sends a request to a url and show lenght of content
curl -s "$1" | wc -c