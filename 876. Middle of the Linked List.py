# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = []
        curr  = head

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        c = len(res)//2
        curr = head
        i=0
        while curr:
            if i==c:
                break
            
            curr = curr.next
            i+=1
        return curr
        

        