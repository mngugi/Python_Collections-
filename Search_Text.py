# this code is used for searching texts 
# here we search the words monstrous in Moby Dick
# search for the words
#Sense and Sensibility for the word affection, using text2.concord
#ance("affection"). Search the book of Genesis to find out how long
#some people lived, using: text3.concordance("lived"). You could look
#at text4, the Inaugural Address Corpus, to see examples of English going
#back to 1789, and search for words like nation, terror,god
# concordance permits us to see words in context

from nltk.book import *
print ("   ")
print ("--- Search monstrous in Moby Dick ----!")
text1.concordance("monstrous")
print ("   ")
print ("--- Search affection in Sense and Sensibility using text2 ----!")
text2.concordance("affection")
print ("   ")
print ("--- Search lived in the book Genesis using text3 ----!")
text3.concordance("lived")
print ("   ")
print ("--- Search for nation,terror and god in the Inaugural Address Corpus using text4 ----!")
text4.concordance("nation")
text4.concordance("terror")
text4.concordance("god")



print (                         "===== end of example1 =====")



