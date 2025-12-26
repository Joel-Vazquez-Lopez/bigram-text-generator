# Bigram Text Generator

This project implements a simple and interactive text generator
for English and Spanish.

Word suggestions are generated using bigram frequency extracted from a small
reference corpus. When there is no possible continuation, the user can either
choose from random lexicon entries or input a custom word.

The system includes a simple spell-checking mechanism based on edit distance.

## Requirements
- Python 3
- nltk

## Usage
Run the script from the terminal:

```bash
python3 predictor_en.py 
