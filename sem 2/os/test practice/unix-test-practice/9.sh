#!/bin/bash
# Write a script that finds in a given directory hierarchy, all duplicate files and displays their paths. Hint: use checksums to detect whether two files are identical.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

