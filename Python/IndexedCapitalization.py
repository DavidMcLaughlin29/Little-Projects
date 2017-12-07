def capitalize_indices(s, ind=[]):
    """
    Given a string and an array of integers representing indices, capitalize all letters at the given indices.

    """
    result = []
    for index, item in enumerate(s):
        if index in ind:
            result.append(item.upper())
        else:
            result.append(item)
    return "".join(result)


print(capitalize_indices('string', [1, 2, 3]))
