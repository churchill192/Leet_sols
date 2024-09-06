# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head

        while current:
            length+=1
            current = current.next
        
        if length==1:
            return None
        elif length==2:
            if n==2:
                dummy = ListNode(0,head.next)
                return dummy.next
            else:
                head.next = None
                return head

        else:
            dummy = ListNode(0,head)

            x = length-n
            i=0
            slow = head
            fast = head.next
            while slow and fast:
                if i==x:
                    dummy.next=head.next
                    break
                if i==x-1:
                    slow.next = fast.next
                    break
                else:
                    i+=1
                slow = slow.next
                fast = fast.next
            return dummy.next

        