class Solution(object):
    def delete_node(self, node):
        nextNode = node.next
        node.value = nextNode.value
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)