# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:28:43 2017

@author: nhowlett
"""

from data import *
import random

# - Draw random sample
play_letters = random.sample(POUCH, 7)

print('Letters Drawn:', *play_letters)

candidate = input("Form a valid word:")


letters_test = play_letters[:]

valid = False

while not valid:
    candidate = input("Form a valid word:")
    if len(candidate) > 7:
        print("Candidate word too long, cheating is for losers.")
    else:
        for idx in range(len(candidate)):
            letter = candidate[idx]
            if letter in letters_test:
                letters_test.remove(letter)
                if(len(letters_test) == 0):
                    valid = True
            else:
                print("Letter", letter, "not in drawn letters, cheating is for losers.")
                break
