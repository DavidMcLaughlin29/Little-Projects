# def WordsToLowerCase(listofwords):
#     lowercasewords = []
#     for word in listofwords:
#         lowercasewords.append(word.lower())

#     return(lowercasewords)


# list = ["Cool", "SamSung", "johnYYsU"]

# print(WordsToLowerCase(list))

# lowerCaseWords = WordsToLowerCase(list)


# def checkforduplicates(listofwords):
#     index = 0
#     for word in lowerCaseWords(listofwords):
#         if word[index] == word[index + 1]:
#             return true
#         index = index + 1
#     return false


# isDuplicate = checkforduplicates(list)


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
