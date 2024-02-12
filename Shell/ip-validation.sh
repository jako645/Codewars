#!/bin/bash

ip_address=$1
rx="(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

if ! [[ $ip_address =~ ^$rx\.$rx\.$rx\.$rx$ ]]; then
  echo "False"
else
  echo "True"
fi
