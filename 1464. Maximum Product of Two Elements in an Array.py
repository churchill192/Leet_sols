class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    x = (nums[i]-1)*(nums[j]-1)
                    res.append(x)
        return max(res)