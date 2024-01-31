#!/bin/bash

cats_shelves() {
  start_shelve=$1
  stop_shelve=$2
  echo $(( (stop_shelve - start_shelve) / 3 + (stop_shelve - start_shelve) % 3 ))
}

cats_shelves "$@"
