# this a python program that converts the
# character in a string or word and makes
# it an upper case.

user_input = str(input("Enter a Phrase: ")) # user inputs a word
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[2]).upper()

print(Acronyms)