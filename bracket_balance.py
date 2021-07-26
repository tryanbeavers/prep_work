# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
#
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the
# left of a closing bracket (i.e., ), ], or }) of the exact same type.
# There are three types of matched pairs of brackets: [], {}, and ().
#
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.
# For example, {[(])} is not balanced because the contents in between { and } are not balanced.
# The pair of square brackets encloses a single, unbalanced opening bracket, (, and the
# pair of parentheses encloses a single, unbalanced closing square bracket, ].
#
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
#
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given  strings of brackets, determine whether each sequence of brackets is balanced.
# If a string is balanced, return YES. Otherwise, return NO.

# STDIN Function ----- -------- 3 n = 3 {[()]} first s = '{[()]}' {[(])} second s = '{[(])}' {{[[(())]]}} third s ='{{[[(())]]}}'

# OUTPUT:  YES NO YES

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    balanced_stack = []
    char_list = list(s)

    for char in char_list:
        #Open characters add to the stack
        if char in open_list:
            balanced_stack.append(char)
        elif char in close_list:
            same_type = close_list.index(char)
            #close characters remove from the stack if they are the same type
            if len(balanced_stack)>0 and open_list[same_type] == balanced_stack[len(balanced_stack)-1]:
                balanced_stack.pop()
            else:
                return("NO")

    if len(balanced_stack) == 0:
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':

    strings = ["{[()]}", "{[(])}", "{{[[(())]]}}"]
    for s in strings:
        result = isBalanced(s)
        print(result)


