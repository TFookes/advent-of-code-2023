#!/bin/bash

DAY="$( date | awk ' { print $2 } ' )"
DAYSTR="day$DAY"
echo "Pulling input for day $DAY"
mkdir "$DAYSTR"
cp "./template.py" "$DAYSTR/1.py"
cp "./template.py" "$DAYSTR/2.py"
touch "$DAYSTR/inputs.txt"
touch "$DAYSTR/test_inputs.txt"
OUTPUT="$DAYSTR/inputs.txt"
echo "Writing to file: $OUTPUT"

URL="https://adventofcode.com/2022/day/$DAY/input"
SESSION="53616c7465645f5f8b15ae3fe7a237e9ed28a394c4e12a0143db49dc9c0a4d8bf7d87347900866c77a2dd4be0bcb1b559179328dcf4f72088f5569694cb4b927"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
echo "Happy Solving :)"
