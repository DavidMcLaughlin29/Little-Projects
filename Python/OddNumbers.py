def oddNumbers(l, r):
    listofnumbers = list(range(1, r + 1))
    listofoddnumbers = []
    for num in listofnumbers:
        if num % 2 != 0:
            listofoddnumbers.append(num)
    return listofoddnumbers


print(oddNumbers(1, 15))
