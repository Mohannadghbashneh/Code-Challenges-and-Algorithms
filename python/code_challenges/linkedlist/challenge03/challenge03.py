# Write here the code challenge solution
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        '''A function to add values to the linked list'''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def printAll(self):
        '''A function to print all the values in the linked list'''
        elements = []
        if self.head is None:
            return ("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                elements.append(current.val)
                current = current.next
            return elements

    def removeNthFromEnd(self, n):
        '''A function to remove the nth node from the end of the linked list'''
        slow = self.head
        fast = self.head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return self.head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head