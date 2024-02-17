#!/bin/bash
sumsParts() {
  local input=($1)
  local length=${#input[@]}
  local sums=()
  local total=0

  for (( i = 0; i < length; i++ )); do
    total=$(( total + input[i] ))
  done

  for (( i = 0; i < length; i++ )); do
    sums+=("$total")
    total=$(( total - input[i] ))
  done

  echo "${sums[@]}"
}


sumsParts "$1"
