# Felicia Tao_Project 1: Wordle
# Due October 13

import words
import display_utility
import random

def check_word(secret, guess):
    """ secret is the answer for the game and guess is what the user thinks the answer is, both are strings
    The function will output a list of length 5 containing the strings "grey", "yellow", or "green" to signify
    the status of the letter """
    colors = ["","","","",""] # list keeping track of which letters are right in the guess, the color clue for each letter in guess
    checked = ["","","","",""] # list keeping track of which letters in secret have been checked so that two clues won't come from same letter
    for i in range(len(guess)): # looping through all the letters in the guess
        if guess[i] == secret[i]: # if the answer letter and the guess letter are the same
            colors[i] = "green" # assign the slot that matches the guess slot green
            checked[i] = "yes" # indicates that the spot in the answer was checked
    
    for j in range(len(guess)): # looping through all letters in the guess
        for k in range(len(secret)): # looping through all letters in answer
            if guess[j] == secret[k] and colors[j] == "" and checked[k] == "":
                # if the letter in the guess is the same as the letter in answer, that guess spot is not already green, and the secret letter was not already checked
                colors[j] = "yellow" # assigning that letter in guess with yellow
                checked[k] = "yes" # indicating that this letter in the answer was checked
    
    for z in range(len(guess)): # looping through all letters in guess
        if colors[z] == "": # if not assigned green or yellow
            colors[z] = "grey" # assign that slot grey
    
    return colors # returns a list

def known_word(clues):
    """ clues is a list containing all the guesses taken and clues received so far in a tuple, so [(guess,clue), (guess2,clue2)...]
    The output is the known letters of the answer according to the green hints and positions unknown are presented as _ """
    known = ["_", "_", "_", "_", "_"] # list assuming that nothing is known
    known_string = "" # the final string that stores the known letters + location
    for i in range(len(clues)): # 1st level- looping through each (guess, clue) tuple in the clues list
        for j in range(len(clues[i][1])): # 2nd level- looping through all the color clues in the clue list
            if clues[i][1][j] == "green": # 3rd level- if the string at that index is "green"
                known[j] = clues[i][0][j] # the letter will be added to the known letters string

    for i in range(len(known)): # looping through all strings in known
        known_string += known[i] # add each letter to the string

    return known_string # returns a string of known letters

def no_letters(clues):
    """ clues is a list containing all the guesses taken and clues received so far in a tuple, so [(guess,clue), (guess2,clue2)...]
    The output is a string indicating which letters we know are not in the answer according to the grey hints """
    grey_letters = "" # empty string to store the grey letters
    final_grey = "" # the final string with the grey letters sorted
    for i in range(len(clues)): # looping through each (guess, clue) tuple in the clues list
        for j in range(len(clues[i][1])): # looping through the colors in the clue list, j is the location in the clue list
            if clues[i][1][j] == "grey": # if the clue at j is the string "j"
                if not clues[i][0][j] in yes_letters(clues) and not clues[i][0][j] in grey_letters:
                    # if the letter that is grey is not in the list of letters that are green/yellow or grey
                    grey_letters += clues[i][0][j] # then you add that letter to grey_letters
                
    sorting_grey = list(grey_letters) # changing string into list
    sorting_grey.sort() # putting all the grey letters into alphabetical order
    for k in range(len(sorting_grey)): # for all the sorted letters in the list
        final_grey += sorting_grey[k] # add each letter to the string in alphabetical order

    return final_grey # returning all grey letters in order

def yes_letters(clues):
    """ clues is a list containing all the guesses taken and clues received so far in a tuple, so [(guess,clue), (guess2,clue2)...]
    The output is a string indicating which letters are in the word based on green and yellow hints """
    is_letter = "" # empty string to store letters
    final_letters = "" # the final string with the green/yellow letters sorted
    for i in range(len(clues)): # looping through each (guess, clue) tuple in the clues list
        for j in range(len(clues[i][1])): # looping through the colors in the clue list, j is the location in the clue list
            if clues[i][1][j] == "green" or clues[i][1][j] == "yellow": # if the clue is green or yellow
                if not clues[i][0][j] in is_letter: # if the letter corresponding to the clue is not already in the list
                    is_letter += clues[i][0][j] # add that letter in the list

    sorting_letters = list(is_letter) # changing string into list
    sorting_letters.sort() # putting all the letters in alphabetical order
    for k in range(len(sorting_letters)): # for all the sorted letters in the list
        final_letters += sorting_letters[k] # adding each letter to the list

    return final_letters # returning all green/yellow letters in order

def game(secret):
    """ secret is a string which is the answer, is only valid if it is 5 letters long and in the word list
    Should implement a playable Wordle game and the user gets 6 guesses at the answer
    Before each guess, the current known green, yellow, and grey letters should be printed and after each guess, a complete
    record of the guesses and clues so far should be printed"""
    # print(secret) # to check code
    clues = [] # a list storing (guess, clue) tuples with the user's guess and corresponding clue list in it
    for i in range(6): # only 6 guesses allowed
        print("Known: ", known_word(clues)) # print what is letters are known so far, with the location
        print("Green/Yellow Letters:", yes_letters(clues)) # print which letters are green or yellow so far
        print("Grey Letters:", no_letters(clues)) # print which letters have been tested but are not in the word
        user_guess = input("> ") # user inputs their guess
        while not len(user_guess) == 5: # ask the user to input again if it's not a 5 letter word
            print("Not a word. Try again")
            user_guess = input("> ")
        user_guess = user_guess.upper() # changing input to uppercase
        this_clues = check_word(secret, user_guess) # the color clue list for this guess
        clues.append((user_guess, this_clues)) # appending a tuple with the user guess and corresponding list of clues
        
        for i in range(len(clues)): # loop through each tuple of the guesses made so far and the corresponding clues
            for j in range(len(clues[i][1])): # loop through the colors in the clue list
                if clues[i][1][j] == "green": # if the clue at this location is green
                    display_utility.green(clues[i][0][j]) # print that letter with a green bakground
                elif clues[i][1][j] == "yellow": # if the clue at this location is yellow
                    display_utility.yellow(clues[i][0][j]) # print that letter with a yellow background
                else: # the clue if not green or yellow
                    display_utility.grey(clues[i][0][j]) # print that letter with a grey background
            print() # go to next line for next word

        if user_guess == secret: # if the guess is correct
            print("Answer:", secret)
            return None

    print("Answer:", secret) # if all 6 guesses have been used, print the answer
    return None

if __name__ == "__main__":
    secret_word = random.choice(words.words) # choosing a random word from the list of words provided
    secret_word = secret_word.upper() # changing the word to uppercase
    game(secret_word) # play game
    