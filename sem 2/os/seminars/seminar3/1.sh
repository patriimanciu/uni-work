#!/bin/bash

COUNT=0
F=$1
while [ $COUNT -lt 100 ]; do
    X=$(cat $F)
    X=$((X+1))
    echo $X > $F
    COUNT=$((COUNT+1))
done
