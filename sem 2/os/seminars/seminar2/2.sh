#!/bin/bash
# write a shell script that takes as arguments pairs of arguments (filename, number)
# for each pair, check if the file size if less than the given num

size=0
while [ $# -eq 2 ]; do
    echo "args: $@"
    file=$1
    num=$2
    if [ -n $file ] && [ -f "$file" ]; then
        fsize=`du -s --block-size=1 $file | awk '[print $1]'`
        if [ $fsize -lt $num ]; then
            echo "File $file has size $fsize which is smaller than $num"
        else
            echo "File $file has size $fsize which is greater than $num"
        fi
        size=$(($size + $fsize))
    fi
    shift 2
done

echo "Total size: $size"
