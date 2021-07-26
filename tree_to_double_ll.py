# Trees: Convert binary tree to doubly linked list
# Convert a binary tree to a doubly linked list so that the order of the
# doubly linked list is the same as an in-order traversal of the binary tree.
#
# After conversion, the left pointer of the node should be pointing to the previous node in
# the doubly linked list, and the right pointer should be pointing to the next node in the doubly linked list.

# root = Node(10)
# root.left = Node(12)
# root.right = Node(15)
# root.left.left = Node(25)
# root.left.right = Node(30)
# root.right.left = Node(36)

# root = Node(100)
# root.left = Node(50)
# root.right = Node(200)
# root.left.left = Node(25)
# root.left.right = Node(75)
# root.left.left.left = Node(30)
# root.left.right.left = Node(60)
# root.right.left = Node(125)
# root.right.right = Node(350)

#output 1 = 25 12 30 10 36 15
#output 2 = 30 25 50 60 75 100 125 200 350

#TAKEN FROM EXAMPLE
class Node(object):
    """Binary tree Node class has
    data, left and right child"""

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def process_tree(root):

    #bottom out here
    if root is None:
        return root

    #first lets process the left side of the tree
    if root.left:

        left = process_tree(root.left)

        while left.right:
            left = left.right

        #The left should refer back to the root it came from
        left.right = root
        #the root's left should now be it's left
        root.left = left

    #we also need to process the right side if it's there
    if root.right:

        right = process_tree(root.right)

        while right.left:
            right = right.left

        #rights left should now point back to the root at this point
        right.left = root
        #and the root should now point to the right
        root.right = right

    return root


def tree_to_double_ll(root):

    flat_tree = process_tree(root)

    #head of the LL is now the left most node tree node
    while flat_tree.left:
        flat_tree = flat_tree.left

    return flat_tree


def print_head_to_tail(head):
    while head:
        print(str(head.data))
        head = head.right


# Driver Code
if __name__ == '__main__':
    root = Node(100)
    root.left = Node(50)
    root.right = Node(200)
    root.left.left = Node(25)
    root.left.right = Node(75)
    root.left.left.left = Node(30)
    root.left.right.left = Node(60)
    root.right.left = Node(125)
    root.right.right = Node(350)


    head = tree_to_double_ll(root)
    print_head_to_tail(head)