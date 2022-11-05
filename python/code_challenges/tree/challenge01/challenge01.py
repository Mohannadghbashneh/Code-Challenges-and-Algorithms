# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:

    def buildTree(self,preorder,inorder):
        '''builds a tree from a preorder and inorder traversal'''
    
        if not preorder or not inorder:
            return None

        if len(preorder) == 1:
            return Node(preorder[0])
        
        root = Node(preorder[0])
        root_index = inorder.index(preorder[0])
    
        root.left = self.buildTree(preorder[1:root_index + 1],inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:],inorder[root_index + 1:])
        
        return root