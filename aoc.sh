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
SESSION="53616c7465645f5f64fc9a22be9a03346c322067a0dabe45ca85772a051be5c44a79b8a03285274fe0fea233ed1680c578afa8ac260165f033a4a5caca55b5067"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
echo "Happy Solving :)"
