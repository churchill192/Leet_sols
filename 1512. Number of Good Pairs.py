class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        res = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i!=j) and (i<j) and (nums[i]==nums[j]):
                    x = [i,j]
                    if x not in res:
                        res.append(x)
        
        return len(res)
        