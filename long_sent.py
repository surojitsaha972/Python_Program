str1=input("Enter a sentence:- ")
words =str1.split()
longest_word=""
for i in words:
    if len(i) > len(longest_word):
        longest_word=i
print("The longest word is: ",longest_word," and length of the word is: ",len(longest_word))