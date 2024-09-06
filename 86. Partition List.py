# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        greaterThanX = []
        lesserThanX = []
        
        curr = head
        while curr:
            if curr.val>=x:
                greaterThanX.append(curr.val)
            else:
                lesserThanX.append(curr.val)
            curr = curr.next
        
        l = ListNode(0)

        curr = l

        for i in lesserThanX+greaterThanX:

            curr.next = ListNode(i)
            curr = curr.next
        return l.next
        
        
        