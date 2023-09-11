import pyfiglet
import random

font = random.choice(pyfiglet.FigletFont.getFonts())
ascii_art = pyfiglet.figlet_format("HAPPY BIRTHDAY TO YOU!", font=font)

greetings = f"\nHAPPY BIRTHDAY TO YOU!\n{ascii_art}"

print(greetings)


