#±/bin/bash
# read until stop, check if it starts with a vowel

CNT=0
while true; do
    read w
    if [[ $w == "stop" ]]; then
        break
    fi
    if [[ $w == [aeiou]* ]]; then
        CNT=$((CNT+1))
    fi
done
echo "Total: $CNT"
