class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        x = {}
        res = []
        for i in range(1,len(nums)+1):
            x[i] = 0
        
        for i in nums:
            x[i]+=1
        
        for key, value in x.items():
            if value == 0:
                res.append(key)
        
        return res

       
    
        
        