
# Score of each letter in scrabble
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

# Dictionary to map a letter lookup with a particular score
LETTER_SCORES = {}
for score, letters in scrabble_scores:
    for letter in letters.split():
        LETTER_SCORES[letter] = score

# Some quick checks on the above
assert LETTER_SCORES['A'] == 1
assert LETTER_SCORES['Q'] == 10
assert sum(LETTER_SCORES.values()) == 87


# The following are only used in Part 2 ------------------------------------------------------------

# Obtained from http://scrabblewizard.com/scrabble-tile-distribution/
scrabble_amounts = [(1, "J K Q X Z"), (2, "B C F H M P V W Y"), (3, "G"),
                    (4, "D U S L"), (6, "N R T"), (8, "O"), (9, "A I"), (12, "E")]

# List of single character strings, repeated in proportion to the tiles available in scabble
POUCH = []
for amount, letters in scrabble_amounts:
    for letter in letters.split():
        POUCH.extend(list(amount * letter))

# Check we have the right number (no blanks in this simple game)
assert len(POUCH) == 98
