#!/bin/bash

longest () {
  sorted_string=""
  input="$1$2"
  for letter in {a..z}
  do
    [[ $input == *$letter* ]] && sorted_string+=$letter
  done
  echo $sorted_string
}

longest $1 $2
