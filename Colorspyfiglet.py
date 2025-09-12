
#Available Colors

#With termcolor, you can use:

#grey, red, green, yellow, blue, magenta, cyan, white
from pyfiglet import Figlet
from termcolor import colored
from colorama import init

# Initialize colorama for Windows compatibility (does nothing on Linux/macOS)
init()
#
# Create pyfiglet text
f = Figlet(font='slant')
ascii_art = f.renderText('Hello!')

# Colorize the ASCII art
colored_art = colored(ascii_art, 'yellow')

print(colored_art)
