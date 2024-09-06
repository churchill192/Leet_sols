class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = []
        l = 0
        r = len(nums)-1
        while l<=r:
            if abs(nums[l]) < abs(nums[r]):
                s.append(nums[r]**2)
                r-=1

            elif abs(nums[r]) < abs(nums[l]):
                s.append(nums[l]**2)
                l+=1

            elif abs(nums[l]) == abs(nums[r]):
                s.append(nums[r]**2)
                r-=1

        return s[::-1]

        # s = []
        # for i in nums:
        #     s.append(i**2)
        # x = sorted(s)
        # return x

        