import tkinter as tk
from collections import defaultdict
from tkinter import StringVar
from nltk.corpus import brown
from better_profanity import profanity
import nltk

nltk.download('brown', quiet=True)

def preprocess_text():
    # Përpunimi i korpusit duke përdorur list comprehensions për performancë më të mirë
    return [[word.lower() for word in sentence if word.isalpha()]
            for sentence in brown.sents() if len(sentence) > 1]

def build_markov_chain(corpus):
    transition_matrix = defaultdict(list)  # Mbaj tranzicionet në një listë të renditur
    prefix_dict = defaultdict(set)

    for sentence in corpus:
        for i in range(len(sentence) - 1):
            current_word = sentence[i]
            next_word = sentence[i + 1]

            # Shto tranzicionet e normalizuara
            transition_matrix[current_word].append(next_word)

            # Ndërto Trie për prefikset
            for j in range(1, len(next_word) + 1):
                prefix = next_word[:j]
                prefix_dict[prefix].add(next_word)

    # Normalizimi i tranzicioneve dhe renditja
    for word, transitions in transition_matrix.items():
        freq = defaultdict(int)
        for next_word in transitions:
            freq[next_word] += 1
        transition_matrix[word] = sorted(freq.items(), key=lambda x: -x[1])

    return transition_matrix, prefix_dict