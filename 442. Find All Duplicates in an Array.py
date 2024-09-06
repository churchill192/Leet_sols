class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        x = {}
        res = []
        for num in nums:
            if num not in x:
                x[num] = 1
            else:
                x[num] += 1
        
        for key, value in x.items():
            if value == 2:
                res.append(key)

        return res

        # seen = set()
        # duplicate = []

        # for num in nums:
        #     if num in seen:
        #         duplicate.append(num)
        #     seen.add(num)
        # return duplicate
        