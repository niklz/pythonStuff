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
    else:
        letters_test = [x.lower() for x in play_letters]
        check =  len(candidate)
        for idx in range(check):
            letter = candidate[idx]
            if letter in letters_test:
                letters_test.remove(letter)
                check -= 1
                if(check == 0):           
                    valid = True
            else:
                print("Letter '"+letter.upper()+"' not in drawn letters, cheating is for losers.")
                break
            
print("Okay, '"+candidate.upper()+"'. What a great word!")

# - find best word
#   Coarse filter
r = re.compile('^['+candidate+']+$')
wordsFilter = filter(r.match, words.lower())
wordsFilter = list(wordsFilter)
#   Fine filter
for word in wordsFilter:
    if len(word) > 7:
        wordsFilter.remove(word)


#- Score the words
scores = scrabs.calc_list_values(wordsFilter)

