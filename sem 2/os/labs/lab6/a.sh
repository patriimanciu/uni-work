#!/bin/bash
echo "Hello World, $1!"

for A in $@; do
    echo "$A"
done
