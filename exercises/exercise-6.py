# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Input a word: "))

reverse=word[::-1]

if word == reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")