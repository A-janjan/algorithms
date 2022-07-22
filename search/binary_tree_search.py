# node of tree
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

# binary tree search
def search(node, value):
    if node == None:
        return False
    if node.value == value:
        return True
    if value<node.value:
        return search(node.left, value)
    return search(node.right, value)

# insert new node
def insert(node, value):
    if value <= node.value:
        if node.left is None:
            child = Node(value, node)
            node.left = child
            return
        insert(node.left, value)
    else:
        if node.right is None:
            child = Node(value, node)
            node.right = child
            return
        insert(node.right, value)