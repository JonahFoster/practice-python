# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
import sys

number = int(input("Input a number: "))
x = list(range(2, number-1))

for num in x:
    if number % num != 0:
        continue
    elif number % num == 0:
        sys.exit("Not a prime number.")
sys.exit("It is a prime number.")