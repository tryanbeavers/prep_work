#!/bin/python3

import math
import os
import string
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

#1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
#zaba
# Should return 28

def designerPdfViewer(h, word):

    alpha_map = dict.fromkeys(string.ascii_lowercase, 0)
    for k, v in enumerate(alpha_map):
        alpha_map[v] = h[k]

    max = 0
    char_arr = list(word)
    for c in char_arr:
        if alpha_map[c] and alpha_map[c] > max:
            max = alpha_map[c]

    if max > 0:
        return len(word) * max

if __name__ == '__main__':


    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
    word = "zaba"

    result = designerPdfViewer(h, word)
    print(result)
