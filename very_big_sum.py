# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
#
# Function Description
#
# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
#
# aVeryBigSum has the following parameter(s):
#
# int ar[n]: an array of integers .
# Return
#
# long: the sum of all array elements
# Input Format
#
# The first line of the input consists of an integer .
# The next line contains  space-separated integers contained in the array.
#
# Output Format
#
# Return the integer sum of the elements in the array.
#
# Constraints
#
#
# Sample Input
#
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Output
#
# 5000000015
# Note:
#
# The range of the 32-bit integer is .
# When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.


import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005

def aVeryBigSum(ar1, ar2):
    split_len = ar1
    to_sum = ar2.split()

    #Make all of them ints
    for k,v  in enumerate(to_sum):
        to_sum[k] = int(v)

    product = int(math.fsum(to_sum))

    print(to_sum)
    print(product)

if __name__ == '__main__':
    ar1 = "5"
    ar2 =  "1000000001 1000000002 1000000003 1000000004 1000000005"
    result = aVeryBigSum(ar1, ar2)

