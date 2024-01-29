#!/bin/sh

base=$1
factor=$2
[ $(($base % $factor)) -eq 0 ] && echo "true" || echo "false"
