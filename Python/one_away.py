# Given two strings, write a function to check if they are one edit (or zero edits) away.

def off_by_one(s1, s2):
    '''Function to determine if two strings are off by one character'''
    if len(s1) == len(s2):
        return can_replace(s1, s2)
    elif len(s1) == len(s2) - 1:
        # s1 is shorter than s2. See if you can insert into s1
        return can_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        # s2 is shorter than s1. See if you can insert into s2
        return can_insert(s2, s1)
    else:
        return False

def can_replace(s1, s2):
    '''Function to determine if you can you replace a character in s1 to get s2'''
    found_difference = False
    for index, character in enumerate(s1):
        if s1[index] != s2[index]:
            if found_difference == True:
                return False
            found_difference = True
    return True


def can_insert(s1, s2):
    '''Function to determine if you can you insert a character in s1 to get s2'''
    for index, character in enumerate(s1):
        if s1[index] != s2[index]:
            if s1[index:] == s2[index + 1:]:
                return True
            return False
    return True

if __name__ == '__main__':
    # Will try to replace a character
    print('pale, bale should be True ->', off_by_one('pale', 'bale'))
    print('pale, bake should be False ->', off_by_one('pale', 'bake'))
    # Will try to insert a character
    print('pale, pales should be True ->', off_by_one('pale', 'pales'))
    print('ple, pale should be True ->', off_by_one('ple', 'pale'))
    print('pale, bales should be False ->', off_by_one('pale', 'bales'))
    # Will flip input and then try to insert a character
    print('pale, ple should be True ->', off_by_one('pale', 'ple'))
    print('pales, pale should be True ->', off_by_one('pales', 'pale'))
    print('pale, pa should be False ->', off_by_one('pale', 'pa'))
