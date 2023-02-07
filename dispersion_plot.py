#we can also determine the location of a word in the text: how many words from the beginning it appears. 
#This positional information can be displayed using a dispersion plot. Each stripe represents
#an instance of a word, and each row represents the entire text.

from nltk.book import * 
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
print ("   ")

text4.dispersion_plot(["citizens","freedom"])

