"""
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
"""


def title_case(title, minor_words=''):
    if title == '' and minor_words == '':
        return ''
    title = title.lower().split()
    minor_words = minor_words.lower().split()
    result = []
    result.append(title[0].capitalize())
    for word in title[1:]:
        if word in minor_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    return ' '.join(result)


print(title_case("", ""))

print(title_case("The World Of Mice", "of"))
print(title_case("The Sea Of Stew", "of"))
print(title_case("the black to wice", "the to"))
print(title_case("isntance of The bumblebees", "of the"))
print(title_case("The World Of Mice", "of"))
