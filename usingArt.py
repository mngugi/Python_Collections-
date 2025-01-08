import pyfiglet

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

def display_title(title):
    border = "*~" * (len(title) // 2 + 1)
    print(border)
    print(f"   {title}")
    print(border)    

if __name__ == "__main__":
    display_title("Fancy Title")



if __name__ == "__main__":
    display_title("My Fancy Title")

