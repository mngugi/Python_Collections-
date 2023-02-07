#The term common_contexts allows us to examine just the contexts that are shared by
#two or more words, such as monstrous and very. We have to enclose these words by
#square brackets as well as parentheses, and separate them with a comma:

from nltk.book import*

print("  ")
print("Common Contexts")
text2.common_contexts(["monstrous","very"])

print ("Common contexts for nation, terror and god")
text4.common_contexts(["nation","terror","god"])

