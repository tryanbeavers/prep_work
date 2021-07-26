# Trees: Level order traversal of binary tree
# Given the root of a binary tree, display the node values at each level.
# Node values for all levels should be displayed on separate lines.

#TAKEN FROM EXAMPLE



class Node(object):
    """Binary tree Node class has
    data, left and right child"""

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def process_level(current_level, q_current):
    q_next = []
    print("LEVEL #" + str(current_level))
    while (len(q_current) > 0):
        print(q_current[0].data)
        element = q_current.pop(0)

        # try to add each child to keep the queue going
        if element.left is not None:
            q_next.append(element.left)
        if element.right is not None:
            q_next.append(element.right)
    print("\n")
    return q_next

def level_order_tree(root):
    #start with your queue empty
    current_level = 0
    q_current = []
    q_current.append(root)

    while True:
        if len(q_current) == 0:
            return
        else:
            current_level = current_level+1
            q_current = process_level(current_level, q_current)

if __name__ == "__main__":
    root = Node(100)
    root.left = Node(50)
    root.right = Node(200)
    root.left.left = Node(25)
    root.left.right = Node(75)
    root.right.right = Node(350)

    level_order_tree(root)