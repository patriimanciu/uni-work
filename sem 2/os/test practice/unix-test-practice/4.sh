#!/bin/bash
# Find recursively in a given directory all the symbolic links, and report those that point to files/directories that no longer exist. Use operator -L to test if a path is a symbolic link, and operator -e to test if it exists (will return false if the target to which the link points does not exist)

DIR=$1
if [ -z $DIR ]; then
    echo "Usage: $0 <directory>"
    exit 1
else
    for A in `find $DIR -type l`; do
        if [ ! -e $A ]; then
            echo "$A does not exist"
        fi
    done
fi
