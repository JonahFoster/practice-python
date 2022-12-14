# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

inputNumber = int(input("Input a number: "))
x = list(range(1, inputNumber+1))
divisor = []

for number in x:
    if inputNumber % number == 0:
        divisor.append(number)

print(divisor)
    