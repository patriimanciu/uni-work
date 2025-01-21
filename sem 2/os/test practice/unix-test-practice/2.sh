#!/bin/bash
# Find recursively in a directory all ".c" files having more than 500 lines. Stop after finding 2 such files.

DIR=$1
FOUND=0
if [ -z $DIR ]; then
    echo "Please provide a directory"
else
    find $DIR -name "*.c" | while read FILE; do
        LINES=$(wc -l < $FILE)
        if test $LINES -gt 500; then
            echo $FILE
            FOUND=$((FOUND+1))
        fi
        if test $FOUND -eq 2; then
            break
        fi
    done
fi
