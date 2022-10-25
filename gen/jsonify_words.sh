#!/bin/bash

### from wordle-fr
# collect valid words of length 5
awk 'length == 5' < ../../wordle-fr/mots.txt > ./valid_fr.txt

# convert to json
jq --raw-input . < ./valid_fr.txt| jq --slurp . > ./valid_fr.json

# target words
cp ../../wordle-fr/src/assets/json/drawable-words.json ./target_fr.json
