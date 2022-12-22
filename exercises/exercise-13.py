# Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.


def fibonacciSequence():
    numbersToGenerate = int(input("How many Fibonacci numbers should I generate? "))
    i = 1
    if numbersToGenerate == 0:
        sequence = []
    elif numbersToGenerate == 1:
        sequence = [1]
    elif numbersToGenerate == 2:
        sequence = [1, 1]
    elif numbersToGenerate > 2:
        sequence = [1, 1]
        while i < (numbersToGenerate - 1):
            sequence.append(sequence[i] + sequence[i-1])
            i += 1
    return sequence

print(fibonacciSequence())