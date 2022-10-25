#!/bin/bash

### from wordle-fr
# collect valid words of length 5
awk 'length == 5' < ../../wordle-fr/mots.txt > ./valid_fr.txt

# convert to json
jq --raw-input . < ./valid_fr.txt| jq --slurp . > ./valid_fr.json

# target words
cp ../../wordle-fr/src/assets/json/drawable-words.json ./target_fr.json

### from wordle-it
cp ../../wordle-it/dict/parole.txt ./target_it.txt

# convert to json
jq --raw-input . < ./target_it.txt| jq --slurp . > ./target_it.json
