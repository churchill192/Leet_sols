# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0)
        curr_dummy = dummy
        look = set(nums)
        curr = head

        while curr:
            if curr.val not in look:
                curr_dummy.next = curr
                curr_dummy = curr_dummy.next
            curr = curr.next
        
        curr_dummy.next = None
        
        return dummy.next

        