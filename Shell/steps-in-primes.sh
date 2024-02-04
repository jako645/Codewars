#!/bin/bash

# Function to check if a number is prime
is_prime() {
  local num=$1
  if [ $num -le 1 ]; then
    return 1
  fi
  local i
  for (( i=2; i*i<=num; i++ )); do
    if [ $((num % i)) -eq 0 ]; then
      return 1
    fi
  done
  return 0
}

# Function to find the first pair of prime numbers with a given step
find_prime_pair() {
  local step=$1
  local start=$2
  local end=$3
  local number=$start

  while [ $((number + step)) -le $end ]; do
    if is_prime $number && is_prime $((number + step)); then
      echo "$number $((number + step))"
      return
    fi
    ((number++))
  done
  echo "0 0"
}

find_prime_pair "$@"
