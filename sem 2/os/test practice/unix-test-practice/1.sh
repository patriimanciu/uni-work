#!/bin/bash
# Display a report showing the full name of all the users currently connected, and the number of processes belonging to each of them.

for A in `cat who.fake | awk '{print $1}'`; do
    N=`cat ps.fake | grep $A | uniq | wc -l`
    echo $A $N
done

