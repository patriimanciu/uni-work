#!/bin/bash
# Consider a file containing a username on each line. Generate a comma-separated string with email addresses of the users that exist. The email address will be obtained by appending "@scs.ubbcluj.ro" at the end of each username. Make sure the generated string does NOT end in a comma.

F=$1

if [ -z $F ]; then
    echo "File needed."
    return 1
else
    N=`wc -l $F | awk '{print $1}'`
    C=1
    for A in $(cat $F); do
        if [ $C -eq $N ]; then
            echo -n "$A@scs.ubbcluj.ro "
        else
            echo -n "$A@scs.ubbcluj.ro"
            echo -n ","
        fi
        C=$((C+1))
    done
fi

