#!/bin/bash
# Write a script that receives dangerous program names as command line arguments. The script will monitor all the processes in the system, and whenever a program known to be dangerous is run, the script will kill it and display a message.

process_running_and_kill() {
    P=`ps -ef | grep -E "$1"| awk '{print $2}'`
    if [ -z "$P" ]; then
        return 1
    elif [ "$P" = "$$" ]; then
        return 2
    else
        kill -9 "$P"
        return 0
    fi
}

while true; do
    echo "Checking for dangerous programs..."
    for p in "$@"; do
        if process_running_and_kill "$p"; then
            echo "Dangerous program. Killing $p"
        fi
    done
    echo "sleeping..."
    sleep 1
done

