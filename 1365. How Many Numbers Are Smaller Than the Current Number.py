class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = {}
        list1=[]
        for i in nums:
            x[i] = nums.count(i)
        

        for i in nums:
            c=0
            for j in x.keys():
                if j<i:
                    c+=x.get(j)
            list1.append(c)
        return (list1)
        