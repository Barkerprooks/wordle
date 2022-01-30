#!/usr/bin/env python3

from sys import argv
from random import choice
from string import ascii_lowercase as alpha

IN = "[WORDLE ATTEMPT %s/6] guess a 5-letter word: "
G = "\033[30m\033[42m"
Y = "\033[30m\033[43m"
C = "\033[0m"

def import_word(path):
    with open(path, "rt") as handle:
        return choice([line.strip() for line in handle.readlines()])

def assert_word(path, word):
    with open(path, "rt") as handle:
        return word in [line.strip() for line in handle.readlines()]

def answer_word(word, wordle):
    
    answers = list(zip(word, [C] * 5))
    matches = dict(zip(word, [0] * 5))

    for i, (guess, actual) in enumerate(zip(word, wordle)):
        if guess == actual:
            matches[guess] = 1
            answers[i] = (answers[i][0], G)
    
    for i, guess in enumerate(word):
        if guess in wordle and not matches[guess]:
            answers[i] = (answers[i][0], Y)

    return answers

def main(args):

    path = "wordle.txt" if len(args) != 2 else args[1]
    
    wordle = import_word(path)
  
    for i in range(1, 7):

        while len(word := input(IN % i)) != 5 or not assert_word(path, word):
            print("not a valid 5 letter word")
       
        answer = answer_word(word, wordle)
        if len(list(filter(lambda x: x[1] != G, answer))) == 5:
            print("you win! the word was:", wordle)
            return 0

        print(''.join(c + l for l, c in answer) + C)

    print("dang, you lose... the answer was:", wordle)
    return 0

if __name__ == "__main__":
    try:
        exit(main(argv))
    except KeyboardInterrupt:
        print("\nok... bye")
        exit(0)
