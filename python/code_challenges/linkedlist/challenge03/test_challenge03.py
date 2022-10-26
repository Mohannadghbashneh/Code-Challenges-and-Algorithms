# Write your test here
import pytest
from challenge03 import LinkedList
from challenge03 import Node


def createLinkedList(list):
    '''A function to take a list as input and append the values to the linked list'''
    ll = LinkedList()
    for i in list:
        ll.append(Node(i))
    ll.printAll()
    return ll





def test_removeNth():
    ll = createLinkedList([1,2,3,4,5,6])
    ll.removeNthFromEnd(2)
    actual = ll.printAll()
    expected = [1,2,3,4,6]
    assert actual == expected

def test_removeNth1():
    ll = createLinkedList([1,2,3,4,5,6,7])  
    ll.removeNthFromEnd(4)
    actual = ll.printAll()
    expected = [1,2,3,5,6,7]
    assert actual == expected

def test_removeNth2():
    ll = createLinkedList(['A','B','C','D','E','F','G'])  
    ll.removeNthFromEnd(6)
    actual = ll.printAll()
    expected = ['A','C','D','E','F','G']
    assert actual == expected

def test_removeNth3():
    ll = createLinkedList(['A','B','C','D','E','F','G','H'])  
    ll.removeNthFromEnd(1)
    actual = ll.printAll()
    expected = ['A','B','C','D','E','F','G']
    assert actual == expected

def test_removeNth3():
    ll = createLinkedList([1,2])  
    ll.removeNthFromEnd(1)
    actual = ll.printAll()
    expected = [1]
    assert actual == expected