#!/bin/bash
n=$1
first_number=$2

echo "$(( ($first_number + ($n / 2)) % $n ))"

