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
- [Limitations](#limitations)
- [Possible Improvements](#possible-improvements)

---

## About
The motivation behind this project is to do an educative implementation in python, 
inspired by predictive text systems 
found in messaging applications like WhatsApp, where the system
suggests possible next words based on the typed input. Rather than
aiming to replicate such systems in terms of performance or scale, this project
focuses on reproducing the core idea at a simplified level: given a word,
suggest plausible continuations based on previously observed usage patterns.
In this case, those patterns are captured through bigram frequency counts
extracted from a reference corpus.

English is used as the primary language due to the availability of richer
linguistic resources. A Spanish version is included as a proof of concept to
demonstrate that the system can be adapted to other languages with minimal
changes to the code.

The goal of the project is not to generate fluent natural language, but to
show how n-gram models work, how they depend on corpus size and lexical
coverage, and how interactive text generation can be implemented using simple
probabilistic theory.



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
based Levenshtein-Damerau distance of 1.

Example interaction:
```text
Enter a word: one
Your entire message was: one
0: day
1: morning
2: time
or enter another word:
```

---

## Installation

### Requirements

- Python 3
- `nltk`

Install dependencies:

```bash
pip install nltk
```

Download the tokenizer data required by NLTK (run once, from python in interactive mode, or in the file.py):
```bash
import nltk
nltk.download("punkt")
```
---

## Usage
Run the script from the terminal, having the lexicon and the corpus in the same directory:

```bash
python3 predictor_en.py
```
To run the Spanish version:
```bash
python3 predictor_sp.py
```

The program runs in an interactive loop. You will be prompted to enter a word,
after which the system will suggest possible next words based on bigram
frequencies.

You can:
- select one of the suggested words by typing its number
- type a custom word manually
- quit the program at any time by typing `q`

---

## Project Structure

```
├── predictor_en.py # English version of the text generator
├── predictor_sp.py # Spanish version of the text generator
├── english.corpus.txt # English reference corpus
├── spanish.corpus.txt # Spanish reference corpus
├── lexicon_en.txt # English lexicon
├── lexicon_sp.txt # Spanish lexicon
├── alpha.txt # English alphabet file
├── alpha_sp.txt # Spanish alphabet file
└── README.md
```
---
## Limitations

- The system relies on raw bigram frequency counts and does not apply any form of smoothing. As a result, unseen word combinations cannot be handled gracefully, thus it doesn't reflect language faithfully.

- Lexical coverage is limited by the size of the provided lexicon. Words not present in the
  lexicon may trigger fallback behavior or require manual input. In spanish is even more conflictive, as for instance, it does not caputure verb forms

- No syntactic or semantic constraints are enforced, so generated sequences may be locally
  plausible but globally incoherent.

- The Spanish version is not optimized for coverage and is included primarily as a proof of
  concept to demonstrate multilingual extensibility.
---

## Possible Improvements

- Improve the size and coverage of both the lexicon and the reference corpus to reduce
  missing words and unavailable continuations.

- Use probabilities instead of raw frequency counts when ranking suggestions, so that
  more likely word combinations are preferred.

- Allow alternative suggestions when the same word appears repeatedly in a sentence,
  instead of always proposing the most frequent continuation.

- Add a simple mechanism to diversify suggestions, for example by avoiding immediate
  repetition of recently selected words.

- Normalize input and corpus text (like handling accented characters in Spanish) to
  reduce sparsity caused by different forms.

