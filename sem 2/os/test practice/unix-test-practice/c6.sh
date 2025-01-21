#!/bin/bash
# cate fisiere cu extensia .txt sunt in directorul curent
# si care contin toate cuvintele date ca parametrii

CNT=0
for A in `find . -type f -name "*.txt"`; do
    C=0
    for B in $@; do
        N=`grep -c "\<$B\>" $A | wc -l`
        if [ $N -eq 0 ]; then
            break
        else
            C=$((C+1))
        fi
    done
    if [ $C -eq $# ]; then
        CNT=$((CNT+1))
    fi
done
echo $CNT

