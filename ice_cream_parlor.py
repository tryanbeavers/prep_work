# Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
#
# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
#
# Example.
#
# The two flavors that cost  and  meet the criteria. Using -based indexing, they are at indices  and .
#
# Function Description
#
# Complete the icecreamParlor function in the editor below.
#
# icecreamParlor has the following parameter(s):
#
# int m: the amount of money they have to spend
# int cost[n]: the cost of each flavor of ice cream
# Returns
#
# int[2]: the indices of the prices of the two flavors they buy, sorted ascending
# Input Format
#
# The first line contains an integer, , the number of trips to the ice cream parlor. The next  sets of lines each describe a visit.
#
# Each trip is described as follows:
#
# The integer , the amount of money they have pooled.
# The integer , the number of flavors offered at the time.
#  space-separated integers denoting the cost of each flavor: .
# Note: The index within the cost array represents the flavor of the ice cream purchased.

# STDIN       Function
# -----       --------
# 2           t = 2
# 4           k = 4
# 5           cost[] size n = 5
# 1 4 5 3 2   cost = [1, 4, 5, 3, 2]
# 4           k = 4
# 4           cost[] size n = 4
# 2 2 4 3     cost=[2, 2,4, 3]

# OUTPUT
# 1 4
# 1 2

def icecreamParlor(m, arr):
    guesser = m - 1
    quick_find = {}
    for k, v in enumerate(arr):
        quick_find[v] = k + 1

    print(quick_find)
    flav1= 0
    flav2= 0
    while guesser > 0:
        if quick_find.get(guesser,None) is not None and quick_find.get(m - guesser,None) is not None:
            #we have a duplicate
            if (quick_find[m - guesser] == quick_find[guesser]):
                for k,v in enumerate(arr):
                    if (v == (m-guesser)) and (k+1 != quick_find[guesser]):
                        flav1 = k+1
                        flav2 = quick_find[guesser]
                        continue
            else:
                flav1=quick_find[m - guesser]
                flav2=quick_find[guesser]
                break
        else:
            guesser = guesser - 1

    if flav1 > flav2:
        return (flav2, flav1)
    else:
        return (flav1, flav2)



if __name__ == "__main__":
    m=4
    arr=[2,2,4,3]
    res = icecreamParlor(m,arr)
    print(res)