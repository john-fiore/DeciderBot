# creation API for DeciderBot
# ----------------------------
# Creator     : John Fiore
# Updated     : 02/05/2025
# File Name   : main.py
# DESC        : main file of DeciderBot

import random as ran
from colorama import Fore
import os
import sys
import resrc.api as db

clr = lambda: os.system('cls')

clist = []
cprfx = ["How about", "I'll choose", "Why not", "Go with", "Try", "The final choice is", "What is"]
prfx_probabilities = [1, 1, 1, 1, 1, 1, 0.1] # 10% chance of getting Jeopardy easter egg

GH_LINK = 'https://github.com/john-fiore/DeciderBot'

def no_cs_inp(prompt): # CS = Case Sensitivity
    return input(prompt).lower()

def decide():
    clr()

    if not clist:
        print(Fore.RED + "Error: No choices available. Returning to main menu.")
        input("Press any key to continue.")
        main()
        return

    color = Fore.YELLOW
    prfix = ran.choices(cprfx, weights=prfx_probabilities, k=1)[0]  # Fixed typo
    final = ran.choice(clist)  # Ensure `clist` is not empty before calling this

    print(prfix + " " + color + final + Fore.RESET)

    print()
    endans = no_cs_inp("Wanna go again? (y/n)")
    
    if endans == "y":
        clist.clear() # make sure to clear choice list before reiterating!
        prompt()
    elif endans == "n":
        main()

def prompt():
    clr()

    optcount = int(input("How many options are there?: "))

    if not isinstance(optcount, int):
        db.ErrPrnt(1, "Enter an INTEGER.")

    for z in range(optcount):
        clist.append(no_cs_inp("Enter Choice: "))

    clr()
    print(f"Is this correct: {clist} (y/n)")
    answr = no_cs_inp("")

    if answr == "y":
        # print("y") - ignore
        decide()
    elif answr == "n":
        clist.clear()
        prompt()

def settings():
    pass

def github():
    db.goToLink(GH_LINK)

def quickclose():
    sys.exit()

def main():
    clr()
    print(Fore.RESET + "Welcome to " + Fore.BLUE + "Decider" + Fore.CYAN + "Bot" + Fore.RESET + "!")
    print()
    print("Please select an option: ")
    print("a) Begin")
    print("b) Settings")
    print("c) GitHub Repo")
    print("d) Quick Close")
    opening_prompt = no_cs_inp("")

    if opening_prompt == "a":
        prompt()
    elif opening_prompt == "b":
        settings()
    elif opening_prompt == "c":
        github()
        main()
    elif opening_prompt == "d":
        quickclose()

if __name__ == "__main__":
    main()