

class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find(root, k):
   
    arr = []

    def Two_Sum_BST(node):
        if not node:
            return False
        x = k - node.val
        if x in arr:
            return True
        else:
            arr.append(node.val)
        return Two_Sum_BST(node.left) or Two_Sum_BST(node.right)

    return Two_Sum_BST(root)