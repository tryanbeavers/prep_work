#!/bin/python3


#
# A left rotation operation on an array shifts each of the array's elements
# unit to the left. For example, if  left rotations are performed on array , then the array would become
# . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.
#
# Given an array  of  integers and a number, , perform  left rotations on the array. Return the
# updated array to be printed as a single line of space-separated integers.

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

# Sample Input
#
# 5 4
# 1 2 3 4 5
#
# Sample Output
#
# 5 1 2 3 4

def rotLeft(a, d):
    start = 0
    while start < d:
        front = a.pop(0)
        a.append(front)
        start = start + 1

    return a

if __name__ == '__main__':

    n = int(5) # size
    d = int(4) # rotations
    a = list("12345")

    result = rotLeft(a, d)
    print(result)

