class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum= sum(nums[:k])
        max_sum = current_sum

        for index in range(len(nums)-k):

            current_sum = current_sum - nums[index]
            current_sum = current_sum + nums[index+k]

            max_sum = max(max_sum,current_sum)
        
        return max_sum/k
        