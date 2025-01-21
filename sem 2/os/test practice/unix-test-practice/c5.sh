#!/bin/bash
# numara cate fiesiere din directorul contin cel putin unul din cuvintele date ca parametri

if [ $# -lt 2 ]; then
    echo "Usage: $0 word1 word2 ..."
    exit 1
fi
DIR=$1
shift 1

if [ ! -d "$DIR" ]; then
    echo "First argument must be a directory"
    exit 1
fi

file=$(mktemp)
for word in $@; do
    for f in `find $DIR -type f`; do
        if grep -q -E "\b$word\b" "$file"; then
            echo $f >> $file
        fi
    done
done
nr=$(sort "$file" | uniq | wc -l)
rm "$file"
echo $nr

