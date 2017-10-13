# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:28:43 2017
@author: nhowlett
"""

from data import *
import random
import re
import scrabs

# - Read dictionary
words = scrabs.load_word_dictionary("words_alpha.txt")

# - Draw random sample
play_letters = random.sample(POUCH, 7)


# - Control flow to accept only a valid candidate word
valid = False
while not valid:
    print('Letters Drawn:', *play_letters)
    candidate = input("Form a valid word: ").lower()
    if len(candidate) > 7:
        print("Candidate word too long, cheating is for losers.")
    elif not scrabs.isWordValid(candidate, play_letters):
        print("One or more of your chosen letters is not in the play letters: cheating is for losers.")
    else:
        break
            
print("Okay, '"+candidate.upper()+"'. What a great word!")

# - find best word
#   Coarse filter
r = re.compile('^['+''.join(play_letters).lower()+']+$')
wordsFilter = filter(r.match, [x.lower() for x in words])
wordsFilter = list(wordsFilter)

wordsCheck = wordsFilter[:]        
for word in wordsFilter:
    if len(word) > 7:
        print("removing (length)"+ word)
        wordsCheck.remove(word)
    else:
        letters_test = [x.lower() for x in play_letters]
        if not scrabs.isWordValid(word, letters_test):
            wordsCheck.remove(word)




#- Score the words
scores = scrabs.calc_list_values(wordsCheck)
print(scores)
