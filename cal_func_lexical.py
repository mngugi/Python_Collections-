# create a function lexical_diversity and another one for percentage
from nltk.book import *
import math 

def lexical_diversity(text):
    return len(text)/len(set(text))
    
    
def percentage(count,total):
    return 100*count/total
    
print ( lexical_diversity(text3))
print (lexical_diversity(text5))
print (percentage(4, 5))
print ( percentage(text4.count('a'), len(text4)))

