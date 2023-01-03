# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order.

sentence = str(input("Input a sentence:"))

def reverseWordOrder():
    splitSentence = sentence.split()
    return " ".join(reversed(splitSentence))

print(reverseWordOrder())
