# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0,head)
        curr = dummy

        while curr and curr.next:
            if res.count(curr.next.val)>1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next

        