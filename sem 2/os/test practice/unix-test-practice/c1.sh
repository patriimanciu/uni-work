#!/bin/bash
# pentru toate literele se creaaza un fisier cu toate cuvintele din f.txt

if [ ! -f $1 ]; then
    echo "$1 trebuie sa fie fisier"
    exit 1
fi

F=$1
shift

for L in "$@"; do
    if [[ $L =~ ^[a-z]$ ]]; then
        grep -E -i -o "\<${L}[a-z]*\>" $F > "$L.txt"
    else
        echo "$L nu este litera"
    fi
done
