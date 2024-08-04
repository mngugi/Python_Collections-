# this a python program that converts the
# character in a string or word and makes
# it an upper case.

user_input = str(input("Enter a Phrase: ")) # user inputs a word
text = user_input.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[0]).upper() # the ith or index position is 0 in the array
# below is the jth or index position is 2 in the array that is converted into lower case
for j in text:
    Acronyms = Acronyms+str(j[2]).lower()

print(Acronyms) # prints out the converted upper and lower case characters