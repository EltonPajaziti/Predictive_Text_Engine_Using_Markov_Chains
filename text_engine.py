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
    transition_matrix = defaultdict(list)  # Mbaj tranzicionet në një listë
    prefix_dict = defaultdict(set)

    for sentence in corpus:
        for i in range(len(sentence) - 1):
            current_word = sentence[i]
            next_word = sentence[i + 1]

            # Shto tranzicionet
            transition_matrix[current_word].append(next_word)

            # Ndërto Trie për prefikset
            for j in range(1, len(next_word) + 1):
                prefix = next_word[:j]
                prefix_dict[prefix].add(next_word)

    # Normalizimi i tranzicioneve dhe llogaritja e probabiliteteve
    for word, transitions in transition_matrix.items():
        freq = defaultdict(int)
        total_count = 0  # Numri total i tranzicioneve për këtë fjalë

        # Numëro frekuencat e fjalëve që ndjekin
        for next_word in transitions:
            freq[next_word] += 1
            total_count += 1  # Rrit numrin total të shfaqjeve

        # Normalizimi për probabilitete
        transition_matrix[word] = sorted(
            [(next_word, count / total_count) for next_word, count in freq.items()],
            key=lambda x: -x[1]
        )

    return transition_matrix, prefix_dict

def predict_next_word(transition_matrix, prefix_dict, sentence_fragment, top_n=5):
    sentence_fragment = sentence_fragment.lower()
    words = sentence_fragment.split()
    if not words:
        return []

    # Nëse ka një hapësirë të fundit, sugjero nga matrica e tranzicionit
    if sentence_fragment.endswith(" "):
        last_word = words[-1]
        if last_word in transition_matrix:
            return [word for word, _ in transition_matrix[last_word][:top_n]
                    if not profanity.contains_profanity(word)]
    else:
        # Nëse nuk ka hapësirë, sugjero nga Trie
        last_word = words[-1]
        if last_word in prefix_dict:
            return [word for word in sorted(prefix_dict[last_word])[:top_n]
                    if not profanity.contains_profanity(word)]

    return []

def build_gui(transition_matrix, prefix_dict):
    suggestions = []
    selected_index = 0

    def on_key_release(event):
        nonlocal suggestions, selected_index
        if event.keysym in ["Up", "Down", "Return"]:
            if event.keysym == "Up" and suggestions:
                selected_index = (selected_index - 1) % len(suggestions)
                update_suggestion_label()
            elif event.keysym == "Down" and suggestions:
                selected_index = (selected_index + 1) % len(suggestions)
                update_suggestion_label()
            elif event.keysym == "Return" and suggestions:
                selected_word = suggestions[selected_index]
                current_text = entry_var.get()

                if current_text.endswith(" "):
                    entry_var.set(current_text + selected_word)
                else:
                    words = current_text.split()
                    words[-1] = selected_word
                    entry_var.set(" ".join(words))
                entry.icursor(tk.END)
                update_suggestion_label()
        else:
            sentence = entry_var.get()
            suggestions = predict_next_word(transition_matrix, prefix_dict, sentence)
            selected_index = 0
            update_suggestion_label()

    def update_suggestion_label():
        suggestion_text = "\n".join(
            [f"> {word}" if i == selected_index else f"  {word}" for i, word in enumerate(suggestions)]
        )
        suggestion_label.config(text=suggestion_text if suggestions else "No suggestions")

    def clear_entry():
        entry_var.set("")
        suggestion_label.config(text="")

    root = tk.Tk()
    root.title("Optimized Predictive Text Engine")
    root.geometry("600x400")

    tk.Label(root, text="Predictive Text Engine", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text="Enter a sentence:").pack()

    entry_var = StringVar()
    entry = tk.Entry(root, textvariable=entry_var, width=60)
    entry.pack(pady=10)
    entry.bind("<KeyRelease>", on_key_release)

    suggestion_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=500, justify="left")
    suggestion_label.pack(pady=10)

    tk.Button(root, text="CLEAR", command=clear_entry).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    print("Processing data... Please wait.")
    corpus = preprocess_text()
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    print("Markov Chain model built with probabilities. Opening GUI...")
    build_gui(transition_matrix, prefix_dict)


