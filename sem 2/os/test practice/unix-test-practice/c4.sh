#!/bin/bash
# delete aparitiile multiplu de trei ale unui cuvant dintr-un fisier
CUV=$2

if [ ! -f $1 ]; then
    echo "Invalid"
    exit 1
fi
count=0
while read line; do
    for cuv in $line; do
        if [ $cuv == $CUV ]; then
            count=`expr $count + 1`
            if [ ! `expr $count % 3` -eq 0 ]; then
                echo $cuv
            fi
        else
            echo $cuv
        fi
    done
done < $1
