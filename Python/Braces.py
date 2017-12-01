def braces(values):
    stack = []
    pushChars = "({["
    popChars = ")}]"
    for char in values:
        if char in pushChars:
            stack.append(char)
        elif char in popChars:
            if not len(stack):
                return "NO"
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(char)]
                print(balancingBracket)
                if stackTop != balancingBracket:
                    return "NO"
        else:
            return "NO"
    return "YES"


test_string = "()[{}]"
# test_string2 = "{}[[])"

test = braces(test_string)
print(test)
# print(braces(test_string2))
