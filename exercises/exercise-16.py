# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random
import string
from random import choices
from string import ascii_letters



letters = choices(ascii_letters, k=7)
numbers = choices(string.digits, k=7)
special = choices(string.punctuation, k=6)
password = letters + numbers + special
finishedPassword = ''.join(password)
print(finishedPassword)