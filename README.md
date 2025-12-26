# Bigram Text Generator

This project implements a simple and interactive text generator
for English and Spanish.

Word suggestions are generated using bigram frequency extracted from a small
reference corpus. When there is no possible continuation, the user can either
choose from random lexicon entries or input a custom word.

The system includes a simple spell-checking mechanism based on edit distance.


---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Demo / Expected Use](#demo--expected-use)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Possible Improvements](#possible-improvements)

---

## About


---

## Features

- English and Spanish support
- Bigram-based next-word suggestions
- Interactive user-driven generation
- Random fallback option when no continuation is available
- Simple spell-checking using Levenshtein-Damerau distance of 1
- Rule-based design (no machine learning)

---


## Demo / Expected Use

The program runs in an interactive loop. Based on the previously selected
word, it proposes possible continuations derived from bigram frequencies.

If no continuation is found, the user can:
- select a random word from the lexicon
- input a custom word manually

When a word is not found in the lexicon, the system may suggest a correction
based on edit distance.

---



## Installation

### Requirements

- Python 3
- `nltk`

Install dependencies:

```bash
pip install nltk

## Usage
Run the script from the terminal:

```bash
python3 predictor_en.py

Download the tokenizer data required by NLTK (run once, from python in interactive mode, or in the file.py):

import nltk
nltk.download("punkt")

