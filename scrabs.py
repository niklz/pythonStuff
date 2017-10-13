# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:05:50 2017

@author: nhowlett
"""

from data import *

# %% function for loading word list 

def load_word_dictionary(filename):
    with open(filename) as f:
        words = f.readlines()        
    # Stripping newline characers
    words = [x.strip().upper() for x in words]
    return words

# %% function for calculating word value

def calc_word_value(word):
    word = word.upper()
    value = 0
    for c in word:
        value += LETTER_SCORES[c]
        
    return value

# %% function for calculating word values for each word in list
def calc_list_values(words):
    wordVals = []
    for word in words:
        wordVals.append((word, calc_word_value(word)))
        
    return wordVals


# %% function for checking if word is contstructable from group of letters
def isWordValid(word, letters):
    letters_test = [x.lower() for x in letters]
    check =  len(word)
    for idx in range(check):
        letter = word[idx]
        if letter in letters_test:
            letters_test.remove(letter)
            check -= 1
            if(check == 0):           
                return True
        else:
            return False
