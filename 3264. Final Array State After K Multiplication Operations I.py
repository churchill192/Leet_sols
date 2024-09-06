class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            x = min(nums)
            ind = nums.index(x)
            nums[ind] = x*multiplier
        return(nums)



        