#!/bin/bash

sqInRect() {
  width=$1
  height=$2

  if (( width == height )); then
    echo "nil"
    exit
  fi

  while (( width != height )); do
    if (( width > height )); then
      width=$(( width - height ))
      squares+=($height)
    else
      height=$((height - width ))
      squares+=($width)
    fi
  done

  squares+=($height)
  echo ${squares[@]}
}

sqInRect $1 $2
