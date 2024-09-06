# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k==0 :
            return head
        
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
       
        k = k%len(nums)        
      

        if k==0:
            res = nums
        else:
            res = nums[-k:] + nums[:-k]
        

        

        #res = nums[k+1:] + nums[:k+1]
        
        l = ListNode(0)
        curr = l
        for i in res:
            curr.next = ListNode(int(i))
            curr = curr.next
        
        return l.next
        