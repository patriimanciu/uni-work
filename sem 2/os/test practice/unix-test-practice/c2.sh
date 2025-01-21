#!/bin/bash
# count ne of occurrences of file in dir1 and subdirectories
# put the result in file
if [ $# -ne 2 ]; then
    echo "Usage: $0 <dir> <file>"
    exit 1
fi

dir=$1
file=$2

if [ ! -d $dir ]; then
    echo "$dir is not a directory"
    exit 2
fi
if [ ! -f $file ]; then
    echo "$file is not a file"
    exit 3
fi
c=`find $dir | grep -E -c "$file$"`
echo "$dir $file $c" >> file.txt
