# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1=""
        str2=""

        while l1:
            #list1.append(l1.value)
            str1+=str(l1.val)
            l1 = l1.next
        
        while l2:
            #list2.append(l1.value)
            str2+=str(l2.val)
            l2 = l2.next
        
        
        x=(list(reversed(str((int(str1[::-1]) + int(str2[::-1]))))))

        l3 = ListNode(0)
        curr = l3
        for i in x:
            curr.next = ListNode(int(i))
            curr = curr.next
        return l3.next
