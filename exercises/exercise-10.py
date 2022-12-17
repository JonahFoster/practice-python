# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
# Write this using at least one list comprehension.
# Extra: randomly generate 2 lists

import random

a = random.sample(range(100), 10)
b = random.sample(range(100), 15)
c = [number for number in a and b if number in a and b]

print(a)
print(b)
print(c)     