class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        minimum_value = arrays[0][0]
        maximum_value = arrays[0][-1]
        max_diff = 0

        for i in range(1,len(arrays)):
            
            a = abs(minimum_value-arrays[i][-1])
            b = abs(maximum_value-arrays[i][0])
            max_diff = max(max_diff, a, b)

            minimum_value = min(minimum_value, arrays[i][0])
            maximum_value = max(maximum_value, arrays[i][-1])
        
        return max_diff
        