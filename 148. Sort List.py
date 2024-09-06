# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        res = sorted(res)

        l = ListNode(0)
        curr = l

        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        
        return l.next
        