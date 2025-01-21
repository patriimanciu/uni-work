#!/bin/bash
# Find recursively in a directory, all the files with the extension ".log" and sort their lines (replace the original file with the sorted content)

DIR=$1
if [ -z "$DIR" ]; then
    echo "Please provide a directory"
else
    for A in `find $DIR -type f -name "*.log"`; do
        sort $A > $A.tmp
        mv $A.tmp $A
    done
fi
