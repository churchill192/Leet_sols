# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        b = []
        c=[]
        for i in range(len(res)):
            if i%2==0:
                b.append(res[i])
            else:
                c.append(res[i])
        x = b+c
        dummy = ListNode(0)
        curr = dummy
        for i in x:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
        

        