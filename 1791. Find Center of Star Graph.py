edges = [[1,2],[2,3],[4,2]]

c = set(edges[0]).intersection(*edges[1:])
for i in c:
    print(i)


"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = set(edges[0]).intersection(*edges[1:])
        for i in c:
            return i
        

"""