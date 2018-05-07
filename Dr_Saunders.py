import os
import re

# Dr Saunders
name = input("Hello, my name is Dr. Saunders. Thank you for joining me today. What is your name?\n")
#TODO: Only grab first name from answer, leaving off any punctuation.
response = re.compile(input("It's nice to meet you, {}. Tell me, how are you feeling today?\n".format(name)))


#('.* (I\'m|I am) (depressed|sad) .*')
if response.search('((I am|I\'m)+ depressed)'):
    print("I am sorry that you are depressed.")
    


