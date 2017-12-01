# Write a function that takes 2 numbers
# and returns a list of the odd numbers
# between them, starting with the first
# and ending with the last (inclusive).


def oddNumbers(l, r):
    listofnumbers = list(range(l, r + 1))
    listofoddnumbers = []
    for num in listofnumbers:
        if num % 2 != 0:
            listofoddnumbers.append(num)
    return listofoddnumbers


n = oddNumbers(100, 1500)


for num in n:
    print num
