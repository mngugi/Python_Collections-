# the python function set() can be used to obtain vocabularies
#By wrapping sorted() around the Python expression set(text3) , we obtain a sorted
#list of vocabulary items, beginning with various punctuation symbols and continuing
#with words starting with A. All capitalized words precede lowercase words. We dis-
#cover the size of the vocabulary indirectly, by asking for the number of items in the set,
#and again we can use len to obtain this number . Although it has 44,764 tokens, this
#book has only 2,789 distinct words, or “word types.”

from nltk.book import *
print ("Sorted text are :")
s=sorted(set(text3))
print(s)

print ("the number of vocabularies in the set is: ")
l=len(set(text3))
print(l)

