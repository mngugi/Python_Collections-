# a python program for handling text

text1 = "The young boys of Malindi have given us a warm welcome. Look out for what they did in the next post 🌊"
i = print('text length is : ', len(text1))
print ('------------------------------------------------------------------------------------------------------')
k = text1.split(' ')
j = len(k)
print(k)
print(j)
print ('------------------------------------------------------------------------------------------------------')
''' 
text1 = "The young boys of Malindi have given us a warm welcome. Look out for what they did in the next post 🌊"

# Get the length of the text
text_length = len(text1)
print('Text length is:', text_length)

# Split the text into words and print them
words = text1.split(' ')
print('Split:', words)

'''

print ('Words with len()>= 4')
words_split = text1.split(' ')
words = [w for w in words_split if len(w) >= 4]
print(words)

'''
text1 = "The young boys of Malindi have given us a warm welcome. Look out for what they did in the next post 🌊"

# Split the text into words
words = text1.split()

# Filter the words with length >= 4
filtered_words = [w for w in words if len(w) >= 4]

# Print the filtered words
print('Words with len() >= 4:', filtered_words)

'''
print ('------------------------------------------------------------------------------------------------------')

print ('Capital words')
words_split = text1.split(' ')
words = [w for w in words_split if  w.istitle()]
print(words)
print ('------------------------------------------------------------------------------------------------------')

print ('Words end with e')
words_split = text1.split(' ')
words = [w for w in words_split if  w.endswith('e')]
print(words)