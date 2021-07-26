# Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its  attribute, insert this node at the desired position and return the head node.
#
# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.
#
# Example
#  refers to the first node in the list
#
#
# Insert a node at position  with . The new list is
#
# Function Description Complete the function insertNodeAtPosition in the editor below. It must return a reference to the head node of your finished list.
#
# insertNodeAtPosition has the following parameters:
#
# head: a SinglyLinkedListNode pointer to the head of the list
# data: an integer value to insert as data in your new node
# position: an integer position to insert the new node, zero based indexing
# Returns
#
# SinglyLinkedListNode pointer: a reference to the head of the revised list
# Input Format
#
# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
# The next line contains an integer , the data of the node that is to be inserted.
# The last line contains an integer .

# Sample input
# 3
# 16
# 13
# 7
# 1
# 2

# Sample output
#16 13 1 7

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data)

        node = node.next


#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    node = llist
    new_item = SinglyLinkedListNode(data)
    #start at the head and go down.
    counter = 0
    while node:
        #if you got to where you want to be put your new node in and modify references
        if counter == position-1:
            new_item.next = node.next
            node.next = new_item

        node = node.next

        counter = counter+1

    return llist

if __name__ == '__main__':

    llist_count = int(3)
    llist = SinglyLinkedList()
    start_list = "16 13 7".split()
    print(start_list)
    for k in range(llist_count):
        llist_item = int(start_list[k])
        llist.insert_node(llist_item)

    data = int(1)
    position = int(2)

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)

