class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        x = {}

        for index in range(len(nums)):

            if nums[index] in x and abs(index - x[nums[index]])<=k:
                return(True)
            else:
                x[nums[index]] = index
        return(False)
        