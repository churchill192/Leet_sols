class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        k = len(nums)
        
        res = []
        for i in range(k):

            current_sum = sum(nums[:k])
            res.append(current_sum)


            for j in range(len(nums)-k):

                current_sum = current_sum - nums[j]
                current_sum = current_sum + nums[j+k]
                res.append(current_sum)

            k-=1
        return(sum(sorted(res)[left-1:right])% (10**9 + 7))

        