# A queue is an abstract data type that maintains the order in which elements were added to it,
# allowing the oldest elements to be removed from the front and new elements to be added to the
# rear. This is called a First-In-First-Out (FIFO) data structure because the first element added
# to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
#
# A basic queue has the following operations:
#
# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process
# queries, where each query is one of the following  types:
#
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.
# Input Format
#
# The first line contains a single integer, , denoting the number of queries.
# Each line  of the  subsequent lines contains a single query in the form described in the problem statement above.
# All three queries start with an integer denoting the query , but only query  is followed
# by an additional space-separated value, , denoting the value to be enqueued.

#INPUT
# 10      q = 10 (number of queries)
# 1 42    1st query, enqueue 42
# 2       dequeue front element
# 1 14    enqueue 42
# 3       print the front element
# 1 28    enqueue 28
# 3       print the front element
# 1 60    enqueue 60
# 1 78    enqueue 78
# 2       dequeue front element
# 2       dequeue front element

# OUTPUT
# 14
# 14

def process_input(commands):
    queue = []

    for com in commands:
        #1 means to enqueue
        if type(com) == tuple:
            queue.append(com[1])
        else:
            #2 means to dequeue
            if com == 2:
                queue.pop(0)
            #3 mean print the first element
            if com == 3:
                print(queue[0])



if __name__ == '__main__':
    query_count = 10
    commands = [(1,42),2,(1,14),3,(1,28),3,(1.60),(1,78),2,2]
    process_input(commands)
