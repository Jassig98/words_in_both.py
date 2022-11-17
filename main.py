# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 15, 2022
# Description: Program that takes two strings and returns words that are in both

def words_in_both(a,b):
    wordsa = set(a.lower().split())
    wordsb = set(b.lower().split())
    result = set()

    for x in wordsa:
        if x in wordsb:
            result.add(x)
    return result
"""function takes two strings and returns words that are in both strings"""