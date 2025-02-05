# creation API for DeciderBot
# ----------------------------
# created by John Fiore
# last updated: 02/05/2025

import webbrowser as wb
from colorama import Fore
from enum import Enum

class ErrType(Enum):
    WARNING = 0,
    ERROR = 1

def goToLink(link: str):
    wb.open(link)

def ErrPrnt(type: ErrType, msg: str):
    if type == ErrType.WARNING:
        print(Fore.YELLOW + "WARNING: " + Fore.RESET + msg)
    elif type == ErrType.ERROR:
        print(Fore.RED + "WARNING: " + Fore.RESET + msg)