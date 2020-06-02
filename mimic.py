#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "DJJD2150, Jaspal Singh, Tiffany McLean, Janell Huyck"

import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # creates a dictionary to store the file's words in as keys and values
    mimic_dict = {}
    # opens file and assigns it to a variable
    with open(filename, "r") as f:
        # reads the file and separates it into lines
        text = f.read()
        words = text.split()
        # creates a variable for the starting word and makes it a string
        previous_word = ""
        # loops through the lines to make words
        for word in words:
            # determines whether or not the previous word already exists 
            # in "mimic_dict".  If it doesn't, it assigns the current word to the 
            # previous word as a value.  If it does, it assigns the current word 
            # to the priorly existing previous word as another value.
            # Also makes the previous word the current word to keep the loop running.
            if previous_word not in mimic_dict:
                mimic_dict[previous_word] = [word]
            else:
                mimic_dict[previous_word].append(word)
            previous_word = word
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    # starts a new string variable that will convert mimic_dict from a dictionary to a string
    # next_list = ""
    # creates a new list to loop through that is 200 words long
    for _ in range(200):
        print(start_word, end=' ')
        nexts = mimic_dict.get(start_word)
        if not nexts:
            nexts = mimic_dict['']
        start_word = random.choice(nexts)
        # assigns the carried over word values/ keys from the prior function to the "random_dict"
        # variable in this function
        # random_dict = mimic_dict[start_word]
        # chooses 200 words at random
        # new_word = random.choice(random_dict)
        # concatenates the words into the "next_list" string
        # next_list += " " + new_word
    # prints the string
    # print(next_list)


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
