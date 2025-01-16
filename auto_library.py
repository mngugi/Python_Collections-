import pyautogui
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Python Acronyms")

pyautogui.scroll(60)

pyautogui.typewrite("SVDSVD", interval=0.5)
pyautogui.moveTo(100,100)

pyautogui.click(clicks=3, interval=1)

#SVDSVD

