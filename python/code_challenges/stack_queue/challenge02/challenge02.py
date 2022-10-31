# Write here the code challenge solution
class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        '''pushes a new node to the top of the stack'''
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''removes the node from the top of the stack, and returns the node’s value'''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        '''returns the value of the node located on top of the stack, without removing it from the stack'''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def empty(self):
        '''returns a boolean indicating whether or not the stack is empty'''
        return self.size == 0
    
    def get_size(self):
        return self.size

def is_Valid(s):
    Parentheses={'(':')','{':'}','[':']'}
    stack=Stack()
    for i in s:
        if i in Parentheses.keys():
            stack.push(i)
        elif i in Parentheses.values():
            if stack.empty():
                return False
            if Parentheses[stack.pop()]!=i:
                return False
    return stack.empty()