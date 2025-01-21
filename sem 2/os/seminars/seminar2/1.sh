#!/bin/bash

# write a shell script that takes any amount of arguments and prints if thaiti':as the name of a
# - regular file
# - directory
# - positive base 10 integer
# - anything else

echo "First argument: $1; Second argument $2"
echo "The 10th argument: ${10}"
echo "Argument count: $#" # argument count
echo "All arguments: $*" # returns it as a string
# echo "All arguments: $@" -> $@ returns it as an array
# echo "All arguments: $#" -> argument count
for a in $@; do
    var=0
    if test -f $a; then
        echo "$a is a regular file"
        var=1
    fi
    if test -d $a; then
        echo "$a is a directory"
        var=1
    fi
    if echo $a | grep -E -q "^[0-9]+$";then
        echo "$a is an integer"
        var=1
    fi
    if test $var -eq 0; then
        echo "$a is something else"
    fi
done
