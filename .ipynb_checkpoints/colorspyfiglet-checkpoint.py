from pyfiglet import Figlet
from colorama import init, Fore, Style
import random

# Initialize colorama
init(autoreset=True)

# Define some colors (you can add more)
colors = [
    Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN,
    Fore.BLUE, Fore.MAGENTA, Fore.WHITE
]

# Create PyFiglet text
f = Figlet(font='slant')
text = f.renderText("HELLO")

# Print each character with a random color
for char in text:
    if char.strip():  # color only non-space characters
        print(random.choice(colors) + char, end="")
    else:
        print(char, end="")  # keep spaces as is
