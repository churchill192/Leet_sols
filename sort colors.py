class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums2 = []
        for i in range(len(nums)):
            nums2.append(min(nums))
            nums.remove(min(nums))

        for i in nums2:
            nums.append(i)
        """
        Do not return anything, modify nums in-place instead.
        """
