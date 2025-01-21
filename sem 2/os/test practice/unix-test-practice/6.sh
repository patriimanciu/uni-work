#!/bin/bash
# Find recursively in a directory, all the files that have write permissions for everyone. Display their names, and the permissions before and after removing the write permission for everybody. You will need to use chmod's symbolic permissions mode, instead of the octal mode we have used in class. The the chmod manual for details.

DIR=$1
if [ -z $DIR ]; then
    echo "Usage: $0 <directory>"
    exit 1
else
    for A in `find $DIR -type f -perm -o=w`; do
        echo "File: $A"
        echo `ls -l $A | cut -d ' ' -f 1`
        chmod go-w $A
        echo `ls -l $A | cut -d ' ' -f 1`
    done
fi

