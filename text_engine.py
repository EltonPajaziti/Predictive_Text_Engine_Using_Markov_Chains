import tkinter as tk
from collections import defaultdict
from tkinter import StringVar
from nltk.corpus import brown
from better_profanity import profanity
import nltk

nltk.download('brown', quiet=True)