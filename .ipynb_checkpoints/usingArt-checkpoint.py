import pyfiglet

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

def display_title(title):
    border = "*~" * (len(title) // 2 + 1)
    print(border)
    print(f"   {title}")
    print(border)    

def display_title(title):
    print("✨" * 5 + f" {title} " + "✨" * 5)

def display_title(title):
    print("═" * (len(title) + 4))
    print(f"  {title}  ")
    print("═" * (len(title) + 4))

if __name__ == "__main__":
    display_title("Fancy Title")


