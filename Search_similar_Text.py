#search for words that appear in a similar range of contexts
#by appending the term similar
#We can find out by appending the term
#then inserting the relevant word in parentheses
from nltk.book import*

print("  ")
print("Print similar range of words from text1")
text1.similar("monstrous")

print("  ")
print("Print similar range of words from text2")
text2.similar("monstrous")
