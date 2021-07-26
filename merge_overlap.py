# Arrays: Merge overlapping intervals
# You are given an array (list) of interval pairs as input where each interval
# has a start and end timestamp. The input array is sorted by starting timestamps.
# You are required to merge overlapping intervals and return a new output array.
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def fill_your_run(start,end):
    full_run = []
    while start <= end:
        full_run.append(start)
        start = start + 1
    return full_run

def merge_overlap(A):
    found_pairs = []
    full_run = []
    for element in A:
        if len(full_run) > 0:
            #we have a set.  Chek if we can't expand it
            start = element[0]
            end = element[1]

            #check if it fits or extends the run
            max =  full_run[len(full_run)-1]
            can_fit = start > full_run[0] and (start < max or start +1 < max)
            if can_fit:
                #extend your run.  This could be better and not remake the entire thing
                full_start = full_run[0]
                full_run = fill_your_run(full_start, end)
            else:
                found_pairs.append((full_run[0],max))
                full_run = fill_your_run(start,end)

        else:
            full_run= fill_your_run(element[0],element[1])

    #make sure you take care of what is left when you're done
    if len(full_run) > 0:
        found_pairs.append((full_run[0], full_run[len(full_run)-1]))

    return found_pairs


if __name__ == "__main__":
    A = [[1,3],[2,6],[8,10],[15,18]]
    output = merge_overlap(A)
    print(output)