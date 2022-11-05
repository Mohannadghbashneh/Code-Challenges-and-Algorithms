# Write your test here
import pytest
from challenge01 import *

def test_build_tree():
    tree = Tree()
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).value == 3
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).left.value == 9
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.value == 20
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.left.value == 15
    assert tree.buildTree([3,9,20,15,7],[9,3,15,20,7]).right.right.value == 7

def test_build_tree2():
    tree = Tree()
    assert tree.buildTree([-1],[-1]).value == -1

def test_build_tree3():
    tree = Tree()
    assert tree.buildTree([1,2,3],[2,1,3]).value == 1
    assert tree.buildTree([1,2,3],[2,1,3]).left.value == 2
    assert tree.buildTree([1,2,3],[2,1,3]).right.value == 3
    
