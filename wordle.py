# ----------------------------------------------------------------------
# Name:      wordle
# Purpose:   implement the wordle game
# Author(s): Bhagyesh Rathi
# Date: 09/04/2022
# ----------------------------------------------------------------------
"""
Implement a wordle game that allows users have 6 chances to guess the
word.

1. Prompt the user for the first attempt.
2.If the guess is not correct, print out the colored guess_word,
then prompt the user for another attempt.
3.If the guess is correct, print out the wordle selected_word and a feedback.
4.Repeat step 2 until the user guess the correct word or until the user
reaches the 6th attempt (at the 6th attempt, print out the wordle selected_word
and a feedback)

"""

import random
import string

# Constant assignments
RED = '\033[91m'  # to print text in red: print(RED + text)
GREEN = '\033[92m'  # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)
SOURCE = '''Hello darkness, my old friend I've come to talk with you again 
Because a vision softly creeping Left its seeds while I was sleeping And the 
vision that was planted in my brain Still remains Within the sound of 
silence In restless dreams, I walked alone, Narrow streets of cobblestone 
beneath the halo of a street lamp I turned my collar to the cold and damp. 
When my eyes were stabbed by the flash of a neon light That split the night 
And touched the sound of silence And in the naked light, I saw Ten thousand 
people, maybe more People talking without speaking People hearing without 
listening People writing songs that voices never shared And no one dared 
Disturb the sound of silence "Fools" said I, "You don't know Silence like a 
cancer grows. Hear my words that I might teach you Take my arms that I might 
reach you" But my words, like silent raindrops fell And echoed in the wells 
of silence And the people bowed and prayed To the neon god they made And the 
sign flashed out its warning In the words that it was forming Then the sign 
said, "The words on the prophets are written on the subway walls In tenement 
halls" And whispered in the sound of silence '''


def choose_wordle(text):
    """
    Randomly chooses a 5-lettered word from a given text
    :param text: (string) text from which to choose the mystery word
                 must be passed as a parameter.  Do NOT use the constant
    :return: (string) the mystery word in uppercase
    """
    # enter your code below and take out the pass statement
    # the function should work with any text passed as a parameter.
    # Do NOT use the SOURCE constant directly inside this function.
    words = text.split()

    # joins all the letters in each word and removes punctuation from each word
    words = [''.join(letter for letter in word if letter not in
                     string.punctuation) for word in words]

    # only choose 5-letter words after the punctuation is removed
    words = [i for i in words if len(i.strip(string.punctuation)) == 5]

    random_word = random.choice(words)
    return random_word


def check(wordle, guess):
    """
    Compare the user input wih the chosen-word by letter and letter

    if both letters and index are the same, color it green
    if the letters are the same, but index is different, color it
    yellow
    if the letter is not in the chosen-word, color it red
    :param wordle: (string) the mystery word
    :param guess: (string) the user's guess
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string

    output = ["" for _ in range(5)]
    # working list
    wordle_list = [letter.upper() for letter in wordle]
    guess_list = [letter.upper() for letter in guess]
    remove_list = list()

    for i in range(len(guess_list)):
        if guess_list[i] == wordle_list[i]:
            output[i] = GREEN + guess_list[i] + DEFAULT
            remove_list.append(i)

    counter = 0
    for index in remove_list:
        index = index - counter
        wordle_list.pop(index)
        guess_list.pop(index)
        counter += 1

    for letter in guess_list:
        if letter in wordle_list:
            output[output.index("")] = YELLOW + letter + DEFAULT
            wordle_list.pop(wordle_list.index(letter))
        else:
            output[output.index("")] = RED + letter + DEFAULT

    string_output = "".join(output)
    return string_output


def all_attempts(wordle):
    """
    printout a feedback for each attempt

    Prompt the user for first attempt
    1. If the attempt is correct, printout the feedback
    2. If the attempt is not correct, prompt the user for another attempt
    3. repeat step 2 until the attempt is correct or until the 6th attempt
    occurs (print out the chosen-word and feedback at the 6th attempt)
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts
             False otherwise
    """
    # enter your code below and take out the pass statement
    # use the check function to build the colored feedback string

    attempt = 1
    wordle = wordle.upper()

    while attempt <= 6:
        print(f'Attempt:{attempt}')
        is_correct = False
        guess_word = None
        while not is_correct:
            guess_word = input("Please enter your 5 letter guess: ").upper()
            if len(guess_word) == 5:
                for letter in guess_word:
                    if not letter.isalpha():
                        break
                else:
                    is_correct = True
        print(check(wordle, guess_word))
        if wordle == guess_word:
            match attempt:
                case 1:
                    print("Genius!")
                    return True
                case 2:
                    print("Magnificent!")
                    return True
                case 3:
                    print("Impressive!")
                    return True
                case 4:
                    print("Splendid!")
                    return True
                case 5:
                    print("Great!")
                    return True
                case 6:
                    print("Phew!")
                    return True
        else:
            attempt += 1
    else:
        return False


def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1.call choose_wordle to get the mystery word in uppercase
    # 2.call all_attempts to give the user 6 tries
    # 3.if the user has not guessed the wordle, print the correct answer

    wordle = choose_wordle(SOURCE)
    done_in_six = all_attempts(wordle)
    if not done_in_six:
        print(f"The correct answer is {wordle.upper()}")


if __name__ == '__main__':
    main()
