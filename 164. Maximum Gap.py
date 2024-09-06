class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        diff=[]
        if len(nums)<2:
            return 0
        else:
            for i in range(len(nums)-1):
                diff.append(abs(nums[i]-nums[i+1]))
        
        return max(diff)
                
                

        