# Predictive Text Engine Using Markov Chains

- **Predictive Text Engine Using Markov Chains**

This project was developed as part of an academic assignment to design a predictive text engine capable of suggesting the next word in a sentence using Markov chains. It leverages a Markov chain model to learn word sequences from a given text corpus and generate accurate predictions.

---

## Introduction

The Predictive Text Engine utilizes:
- **Markov Chains**: A probabilistic model that generates the next word in a sequence based on prior context (bigrams and trigrams).
  
The system is trained on the `Brown Corpus` to calculate transition probabilities and produce high-quality predictions. The application includes an interactive graphical user interface (GUI) to test and refine predictions in real time.

---

## Problem Description

The Predictive Text Engine addresses the challenge of predicting the next word(s) in a sentence fragment using statistical models.

### Requirements:
1. Build a Markov chain model incorporating bigrams and trigrams.
2. Generate predictions based on the input sentence fragment.

### Input:
- A training corpus (`Brown Corpus`) to learn word sequences.
- A user-provided sentence fragment for prediction.

### Output:
- A list of the top 3–5 suggested next words.

---

## Features and Implementation Details

### Key Features:
1. **Markov Chain Model**:
   - Calculates transition probabilities using bigrams and trigrams.
   - Normalizes probabilities for accurate predictions.

2. **Trie Prefix Matching**:
   - Suggests completions for incomplete words by matching prefixes.

3. **Profanity Filter**:
   - Filters out inappropriate suggestions using the `better-profanity` library.

4. **Real-Time Predictions**:
   - Dynamically updates predictions as the user types.

5. **Interactive GUI**:
   - Built with Tkinter, allowing users to interact with predictions.
   - Navigation through predictions using `Up`, `Down`, and `Enter` keys.

---

## Usage Instructions

### Prerequisites:
- Install Python 3.x.
- Install required libraries:
  ```bash
  pip install nltk better-profanity

  
Steps to Run the Application:

1. **Ensure the `nltk` Brown Corpus is downloaded**  
   - This will be handled automatically by the script.

2. **Run the script**  
   Use the following command:
   ```bash
   python text_engine.py
3. **Use the GUI**
   - Enter a sentence fragment.
   - View suggestions dynamically below the input box.
   - Use the `Up` and `Down` keys to navigate through suggestions.
   - Press `Enter` to select a suggestion.

  ## Contributors

This project was collaboratively developed by the following team members:

- **Elton Pajaziti**
- **Adrian Mehaj**
- **Çlirimtar Çitaku**
- **Brineta Uka**


