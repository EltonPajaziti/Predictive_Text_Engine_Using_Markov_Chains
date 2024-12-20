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