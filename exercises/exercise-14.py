# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 7]
b = set()
def noDuplicates():
    for num in a:
        b.add(num)
    return(b)

print(noDuplicates())