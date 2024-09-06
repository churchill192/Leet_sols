class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        x = {}
        res = []

        for num in nums:
            if num not in x:
                x[num] = 1
            else:
                x[num] += 1
        
        sorted_items = sorted(x.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            res.append(sorted_items[i][0])

        return(res)
                
                