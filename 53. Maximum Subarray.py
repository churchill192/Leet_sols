class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        max_sub = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum = current_sum + n
            max_sub = max(current_sum, max_sub)
        return max_sub
        