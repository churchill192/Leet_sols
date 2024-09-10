# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        list1 = []

        for i in lists:
            curr = i
            while curr:
                list1.append(curr.val)
                curr = curr.next
        
        dummy = ListNode(0)
        curr = dummy

        for i in sorted(list1):
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next

        