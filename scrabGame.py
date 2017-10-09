# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:28:43 2017
@author: nhowlett
"""

from data import *
import random

# - Draw random sample
play_letters = random.sample(POUCH, 7)




valid = False

while not valid:
    print('Letters Drawn:', *play_letters)
    candidate = input("Form a valid word:").lower()
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