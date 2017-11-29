def same_letters(str_to_check):
    lowercasestring = str_to_check.lower()
    previous = ''
    for char in lowercasestring:
        if previous == char:
            return True
        previous = char
    return False


string = same_letters("LeTtEr")
print(string)
