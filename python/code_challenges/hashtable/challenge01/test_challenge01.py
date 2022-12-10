
# Write your test here
import pytest

from challenge01 import TreeNode, findTarget

def test_zero():
  
  test = TreeNode(7)
  test.right = TreeNode(2)
  test.left = TreeNode(9)
  
  actual= findTarget(test,11)
  excepted= True
  assert excepted == actual

def test_one():
  
  test = TreeNode(7)
  test.right = TreeNode(2)
  test.left = TreeNode(9)
  
  actual= findTarget(test,1)
  excepted= False
  assert excepted == actual
  
def test_tow():
  
  test = TreeNode()
  actual= findTarget(test,7)
  excepted= False
  assert excepted == actual