#!/bin/bash
# Display all the mounted file systems who are either smaller than than 1GB or have less than 20% free space.
LINE=0
A=`cat df.fake | awk 'NR==1 || ($2 < 1024*1024 || $5 < 20)' | awk 'NR>1 {print $6}'`
echo $A
for line in "$A"; do
    if [ $LINE -eq 0 ]; then
        LINE=1
        echo "First line"
        echo $line
    else
        B=`echo $line | awk '{print $6}'`
    fi
done
