import pytest
from collections import defaultdict
from text_engine import preprocess_text, build_markov_chain, predict_next_word


def test_predict_next_word_empty_string():
    corpus = [["hello", "world"], ["this", "is", "a", "test"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    predictions = predict_next_word(transition_matrix, prefix_dict, "")
    assert predictions == []  # Nuk duhet të sugjerojë asgjë për një input bosh

# Test Kufitar

def test_build_markov_chain():
    corpus = [["hello", "world"], ["hello", "there"], ["world", "hello"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    assert "hello" in transition_matrix  # Duhet të ekzistojë
    assert transition_matrix["hello"]  # Duhet të ketë të paktën një tranzicion
    #Testim që duhet të dalë i suksesshëm

def test_predict_next_word_success():
    corpus = [["hello", "world"], ["hello", "there"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    predictions = predict_next_word(transition_matrix, prefix_dict, "hello ")
    assert predictions == ["world", "there"]  # Sugjerimet duhet të jenë të sakta
   #Testim që duhet të dalë i suksesshëm

def test_predict_next_word_unknown():
    corpus = [["hello", "world"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    predictions = predict_next_word(transition_matrix, prefix_dict, "unknown ")
    assert predictions != []  # Testim gabimor: Fjala nuk ekziston
   #Testim që duhet të dalë i gabueshëm

def test_predict_next_word_two_letters():
    corpus = [["apple", "applesauce", "application"], ["apply", "applied"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    predictions = predict_next_word(transition_matrix, prefix_dict, "ap")
    assert predictions == []  # Testi duhet të dështojë nëse nuk sugjeron fjalë që fillojnë me "ap"

    # Testim që duhet të dalë i gabueshëm


def test_predict_next_word_single_letter():
    corpus = [["a", "apple"], ["a", "ant"], ["a", "awesome"]]
    transition_matrix, prefix_dict = build_markov_chain(corpus)
    predictions = predict_next_word(transition_matrix, prefix_dict, "a")
    assert "apple" in predictions or "ant" in predictions or "awesome" in predictions  # Duhet të sugjerojë një fjalë të mundshme
#Test kufitar