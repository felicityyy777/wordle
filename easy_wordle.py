# Felicia Tao_Project 1: Easy Wordle
# Due October 13

import wordle
import words
import display_utility
import random

def filter_word_list(words, clues):
    """ words is a list of words and clues is a list containing all the guesses taken and clues received so far
    The output is a new word list containing only possible answers from the words input based on the clues"""
    possible_words = [] # list that will contain all the possible answer words
    for i in range(len(words)): # looping through all the words
        not_word = "" # string to determine if the word is not valid to be the answer
        for j in range(len(clues)): # looping through the list of (guess, clue) tuples
            if not wordle.check_word(words[i].upper(), clues[j][0]) == clues[j][1]: # if the clue for the word doesn't match the clue for any guess
                not_word = "yes" # the current word is not a word
        if not_word == "": # if the word matches all the clues so far
            possible_words.append(words[i]) # add that word to the list of possible words
    
    return possible_words

def easy_game(secret):
    """ Implement a playable Wordle game and after each guess, the number of possible words is shown, along with up to 5
    random possible words being displayed"""
    # print(secret) # to check code
    clues = [] # list to store all the (guess, clue) tuples
    for i in range(6): # only 6 guesses
        user_guess = input("> ") # user inputs their guess
        while not len(user_guess) == 5: # ask the user to input again if it is not a 5 letter word
            print("Not a word. Try again")
            user_guess = input("> ")
        user_guess = user_guess.upper() # changes the input to uppercase
        this_clues = wordle.check_word(secret, user_guess) # generate color clues for the guess
        clues.append((user_guess, this_clues)) # add the guess-clue pair to clues list
        for i in range(len(clues)): # loop through each tuple of the guesses made so far and the corresponding clues
            for j in range(len(clues[i][1])): # loop through the colors in the clue list
                if clues[i][1][j] == "green": # if the clue at this location is green
                    display_utility.green(clues[i][0][j]) # print that letter with a green bakground
                elif clues[i][1][j] == "yellow": # if the clue at this location is yellow
                    display_utility.yellow(clues[i][0][j]) # print that letter with a yellow background
                else: # the clue if not green or yellow
                    display_utility.grey(clues[i][0][j]) # print that letter with a grey background
            print() # go to next line for next word
        
        possible_answers = filter_word_list(words.words, clues)
        print(len(possible_answers), "words possible:")
        random.shuffle(possible_answers) # randomly shuffling the possible_answers list
        for i in range(5): # printing only 5 possible answers
            if i < len(possible_answers): # won't cause index out of bounds error if there are less than 5 answers
                print(possible_answers[i])
        
        if user_guess == secret: # if user guesses right
            print("Answer: " + secret)
            return None

if __name__ == "__main__":
    secret_word = random.choice(words.words) # choosing a random word
    secret_word = secret_word.upper() # changing the word to uppercase
    easy_game(secret_word) # will print the answer once game is done