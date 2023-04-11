# the AI is experimental, it knows which letters to avoid but does not know how to place letters that are in the word

# The AI was working but doesnt anymore :(

#import stuff
import time
import re
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# chooses random 5 letter word from list
def getTarget():
    lines = [ line for line in open("english3NEW.txt", "r")]
    target = (random.choice(lines))
    return target

# check user guess to see if it is valid and in the list of words
def checkGuess():
    valid = 0
    temp = ""
    file = open("english3NEW.txt", "r")
    guess = str(input("                 ")).upper()
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~: 1234567890]') # blacklisted characters
    if special_char.search(guess) == None and len(guess) == 5:
        for line in file:
            temp = line
            if guess == temp.replace("\n", ""):
                valid += 1
            else:
                valid += 0
    else:
        valid += 0
    
    if valid > 0:
        pass
    else:
        guess = checkGuess()
    
    return guess

def run():
    win = "n"
    lives = 6
    guesses = 0
    print("                 Please guess a word:") #crude way of leaving a gap
    while lives > 0:
        lettersUsed = [] #stops letters from appearing yellow twice when only 1 instance of the letter is correct
        guess = checkGuess()
        if guess == target.replace("\n", ""):
            print(Fore.GREEN + guess)
            win = "y"
            lives = 0
        else:
            i = 0
            # prints each letter one by one on the same line, checking which colour the letter needs to be 
            while i < 4:
                if guess[i] == target[i]:
                    print(Fore.GREEN + guess[i], end="")
                    lettersUsed.append(guess[i])
                elif guess[i] in target and guess[i] not in lettersUsed:
                    print(Fore.YELLOW + guess[i], end="")
                    lettersUsed.append(guess[i])
                else:
                    print(Fore.WHITE + guess[i], end="")
                i += 1
            if i == 4:
                if guess[i] == target[i]:
                    print(Fore.GREEN + guess[i])
                elif guess[i] in target:
                    print(Fore.YELLOW + guess[i])
                else:
                    print(Fore.WHITE + guess[i])
        lives -= 1
        guesses += 1

    if lives <= 0 and win == "y":
        print(f"You win!\nYou got it in {guesses} tries!")
    else:
        print("You lose! The word was", target)

def checkGuessAI():
    lines = [ line for line in open("whitelist.txt", "r")]
    guess = (random.choice(lines))
    return guess

def runAI():
    win = "n"
    lives = 6
    guesses = 0
    lettersWrong = []
    print("                 Please guess a word:") #crude way of leaving a gap
    while lives > 0:
        fin = False
        lettersUsed = [] #stops letters from appearing yellow twice when only 1 instance of the letter is correct
        whitelist = open("whitelist.txt", "w")
        wordsNEW = open("english3NEW.txt", "r")
        while fin == False:
            for line in wordsNEW:
                valid2 = 0
                for char in line:
                    if char in lettersWrong: #problem area
                        valid2 += 1
                if valid2 == 0:
                    whitelist.write(line)
            whitelist.close()
            fin = True
        guess = checkGuessAI()
        if guess == target.replace("\n", ""):
            print(Fore.GREEN + guess)
            win = "y"
            lives = 0
        else:
            i = 0
            while i < 4:
                if guess[i] == target[i]:
                    print(Fore.GREEN + guess[i], end="")
                    lettersUsed.append(guess[i])
                elif guess[i] in target and guess[i] not in lettersUsed:
                    print(Fore.YELLOW + guess[i], end="")
                    lettersUsed.append(guess[i])
                else:
                    print(Fore.WHITE + guess[i], end="")
                    lettersWrong.append(guess[i])
                i += 1
            if i == 4:
                if guess[i] == target[i]:
                    print(Fore.GREEN + guess[i])
                elif guess[i] in target:
                    print(Fore.YELLOW + guess[i])
                else:
                    print(Fore.WHITE + guess[i])
                    lettersWrong.append(guess[i])
        lives -= 1
        guesses += 1
        time.sleep(0.75)
        print(lettersWrong)

    if lives <= 0 and win == "y":
        print(f"You win!\nYou got it in {guesses} tries!")
    else:
        print("You lose! The word was", target)


# RUN
if __name__ == "__main__":
    mode = int(input("Manual (1) or AI (2): "))
    if mode == 1:
        target = getTarget()
        win = run()
    elif mode == 2:
        target = getTarget()
        win = runAI()


