#!/bin/bash

S=0
for F in `find $1 -type d -name "lab*"`; do
    S=$(($S+1))
done
echo $S
