# Word guessing game (hangman)
# ○
# A list of words will be hardcoded in your program, out of
# which the interpreter will
# ○choose 1 random word.
# ○The user first must input their names
# ○
# Ask the user to guess any alphabet. If the random word
# contains that alphabet, it
# ○will be shown as the output(with correct placement)
# ○Else the program will ask you to guess another alphabet.
# ○Give 7 turns maximum to guess the complete word.

import random

words = ["java", "html", "bash", "nodejs", "php"]


def guess_game():
    # word= words[random.randint(0,len(words)-1)]
    word= "java"
    shorted_word = set(word)
    # print(word)
    tries=7
    guessed_letter =[]
    name=input("please Enter you name: ")
    print(f"welcome {name} lets play : ")
    while tries > 0 and len(shorted_word) > 0:
        guess= input(f"plese {name} Enter alph charcter from the word you have {tries} tries  :")
        if guess in word :
            shorted_word.remove(guess)
            print(f"good gob your guess '{guess}' rigth")
            guessed_letter +=guess

            print([letter if letter in guessed_letter else "_" for letter in word])
            tries-=1
        else:
             print("wrong try again")
             tries -=1
    if tries == 7 :
        print(f"sorry {name} you lost ")
    else:
        print(f"congratulation !!!{name} you wan!! and the word is {word} ")

guess_game()