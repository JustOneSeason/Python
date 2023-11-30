class Tnode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    #8.2
def preorder(n) :
    if n is not None :
        print(n.deat, end=" ")
        preorder(n.left)
        preorder(n.right)

    #8.3
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=" ")
        inorder(n.right)

    #8.4
def postorder(n) :
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = " ")

    #8.6
def count_node(n) :
    if n is None:
        return 0
    else :
        return 1 + count_node(n.left)+count_node(n.right)
    
    #8.7
def count_leaf(n):
    if n is None :
        return 0 
    elif n.left is None and n.right is None :
        return 1
    else :
        return count_leaf(n.left)+count_leaf(n.right)
    
    #8.8
def calc_height(n) :
    if n is None : 
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    
    if (hLeft > hRight) : 
        return hLeft + 1
    else: 
        return hRight + 1