#calculate a measure of the lexical richness of the text. The next example
#shows us that each word is used 16 times on average
from nltk.book import *
import math 
lex = len(text3)/len(set(text3))
print ("  ")
print ("Average use of each word is: ")
print(lex)
print(" ")
print ("Word Count is : ")
lex2 = text3.count("smote")
print(lex2)
print(" ")
print("The percentage of the text from the word is: ")
lex3 =100 * text4.count("a")/len(text4)
print(lex3) 

print(" ")
print ("Word Count is : ")
lex4 = text5.count("lol")
print(lex4)
print(" ")
print("The percentage of the text from the word is: ")
lex5 =100 * text4.count("a")/len(text5)
print(lex5) 
