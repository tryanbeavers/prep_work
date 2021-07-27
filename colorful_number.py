# Colorful Numbers
# February 22, 2015 by Sumit Jain
# Objective: Given a number, find out whether its colorful or not.
#
# Colorful Number: When in a given number, product of every digit of a sub-sequence are different.
# That number is called Colorful Number. See Example
#
# Example:
#
# Given Number : 3245
# Output : Colorful
# Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# this number is a colorful number, since product of every digit of a sub-sequence are different.
# That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40
#
# Given Number : 326
# Output : Not Colorful.
# 326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
from functools import reduce

def determine_colorful(num):
    hash_check = {}
    segments = 1
    char_string = list(str(num))
    print(char_string)

    #If you've got a 0 in here just kick out.
    if "0" in char_string:
        return "Not Colorful"

    while segments < len(char_string):
        size = len(char_string)
        for k,v in enumerate(char_string):
            if segments + k <= size:
                chunk = char_string[k:k+segments]
                for k,v in enumerate(chunk):
                    chunk[k] = int(v)
                print(chunk)
                product = reduce((lambda x, y: x * y), chunk)
                been_done = hash_check.get(product, None)
                if been_done is None:
                    hash_check[product] = True
                else:
                    return "Not Colorful"
        segments = segments+1

    return "Colorful"

if __name__ == "__main__":
    num = 236
    res = determine_colorful(num)
    print(res)