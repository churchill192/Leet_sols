class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # res = []
        # x = {}
        # c=len(nums)//3
        # for i in nums:
        #     x[i] = nums.count(i)

        # for key, value in x.items():
        #     if value>c:
        #         res.append(key)
        # return(res)
        
        x = {}
        res = []
        c = len(nums)//3
        for num in nums:
            if num not in x:
                x[num] = 1
            else:
                x[num]+=1

        for num in x:
            if x[num]>c:
                res.append(num)

        return(res)
