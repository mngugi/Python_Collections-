from textblob import TextBlob

blob = TextBlob("The spellin in engrirsh is not gowod")

correct_syntax = blob.correct()

print("Original statement", blob)
print("Corrected statement", correct_syntax)


