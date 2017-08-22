# Scrabble Game Challenge 

This challenge is broken down into two parts:

1. Write a script to calculate the highest scrabble score form a list of words in a text file. 
2. Extend this code to build up a simple Scrabble-like game on the command line. 

# Part 1

Write a script to read in a series of words from a text file and output the word with the highest 
Scrabble score, along with the score value. The input text file has one word per line.  

### Note:

1. Core data values such as `LETTER_SCORES` are included in the `data.py` file, and should be 
imported into your code to make use of them. 

2. Make sure the script is executable over the command line and takes the name of the file as the first 
and only command line argument. 

3. A file `dictionary.txt` is included to test upon. 

As you write the code, think about how you may be able to breakdown the problem into a series of tasks, 
and then write a function for each task. e.g. include:

* `load_word_dictionary(filename)` - Given a file name and returns a list of words
* `calc_word_value(word)` - Given a word, return its scrabble score
* `max_word_value(word_list)` - Given a list of words, return a tuple of (score, word) for the highest scoring word. 


# Part 2 

Using what we've coded, we now build a simple Scrabble-like game whereby the user is given a random 
set of 7 letters, and asked to build the most valuable word. 

Users should interact with the script via the command line, with an example session running something like: 

``` 
Letters drawn: G, A, R, Y, T, E, V
Form a valid word: gary  << user input
Word chosen: GARY (value: 8)
Optimal word possible: GARVEY (value: 13)
You scored: 61.5
```

The final score should be based on: 

    (score_achieved / maximum_possible) * 100 


### Steps 

The final program should perform the following steps:

1. Load in any necessary data structures either previously created or stored in `data.py`

2. Draw 7 random letters from the `POUCH` variable. This contains a list of letters with frequencies
 equal to those in scrabble (increased frequencies of vowels etc.). 

3. Ask the player to form a word with one or more of the 7 letters of the draw. Hint: Look up the [`input()`](https://docs.python.org/3/library/functions.html#input) function 

4. Validate input for:

    1. all letters of word are in those that are drawn;
    2. word is in the given dictionary of allowed words.

5. Calculate the given word value and show it to the player.

6.  Calculate the optimal word (= max word value) by checking all permutations of the 7 letters of 
the draw, cross-checking with the set of valid words. Hint: looking up elements one at a time in a list is 
going to be slow if the list is large! Consider using one of Pythons [other data structures](https://docs.python.org/3/tutorial/datastructures.html)
to represent the valid words. 

7. Show the player what the optimal word and its value is.

6. Calculate the players score, then display it. 

