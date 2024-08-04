user_input = str(input("Enter a Phrase: "))
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[2]).upper()

print(Acronyms)