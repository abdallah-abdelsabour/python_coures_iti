import random

def hangman():
    word_list = ["python", "javascript", "java", "ruby", "c++"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []
    name = input("What is your name? ")
    print("Hello, " + name, "Time to play hangman!")
    print("Start guessing...")
    turns = 7
    while len(word_letters) > 0 and turns > 0:
        print("You have " + str(turns) + " turns left")
        print("Available letters: " + alphabet)
        guess = input("Guess a letter: ").lower()
        if guess in word_letters:
            word_letters.remove(guess)
            letter_storage.append(guess)
        else:
            turns -= 1
            print("Wrong")
        alphabet = "".join(set(alphabet) - set(letter_storage))
        word_as_list = [letter if letter in letter_storage else "_" for letter in word]
        print("Current word: ", word_as_list)
    if turns == 0:
        print("You lost")
    else:
        print("You won")

hangman()
