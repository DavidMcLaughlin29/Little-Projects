"""

Write a program that prints a staircase of size n.
Input is a single integer. Output is the size of n
using '#' symboles and spaces. The height an base
are the size n. For example 6 would look like this:

                   #
                  ##
                 ###
                ####
               #####
              ######
"""


def print_hashes(num):
  for n in range(1, num + 1):
    spaces = ' ' * (num - n)
    hashes = '#' * n
    print(spaces + hashes)


print_hashes(9)
