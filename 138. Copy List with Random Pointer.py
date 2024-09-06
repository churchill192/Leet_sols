"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy = ListNode(0)
        curr_dummy = dummy
        curr = head

        randDict = {}

        while curr:
            new_node = Node(curr.val,curr.next,curr.random)

            randDict[curr] = new_node
            curr_dummy.next = new_node
            curr_dummy = curr_dummy.next
            curr = curr.next

        curr = head
        while curr:
            if curr.random:
                randDict[curr].random = randDict[curr.random]
            curr = curr.next
        
        return dummy.next
        