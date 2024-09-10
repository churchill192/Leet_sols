# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head


        dummy = ListNode(0)
        curr = dummy
        s = head
        f = head.next
        
        while f:
            gcd = math.gcd(s.val,f.val)

            curr.next = s
            curr = curr.next
            curr.next = ListNode(gcd)
            curr = curr.next
            
            s = f
            f = f.next
        curr.next = s
        return dummy.next
        