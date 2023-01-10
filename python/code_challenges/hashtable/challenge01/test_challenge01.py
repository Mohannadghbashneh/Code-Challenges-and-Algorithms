import pytest
from challenge01 import find, Tree



def test_find_sum():
    tree=Tree()
    tree.root = Tree(7)
    tree.root.left = Tree(4)
    tree.root.right = Tree(8)           
    tree.root.right.right = Tree(10)
    tree.root.left.right = Tree(5)
    tree.root.left.left = Tree(2)    
    assert find(tree.root, 20)==False

def test_find_sum_TRUE():
    tree=Tree()
    tree.root = Tree(7)
    tree.root.left = Tree(4)
    tree.root.right = Tree(8)
    tree.root.right.right = Tree(10)
    tree.root.left.right = Tree(5)
    tree.root.left.left = Tree(2)    
    assert find(tree.root, 13)==True