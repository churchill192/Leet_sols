class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        x = (sorted(dic.keys()))
        l=[]
        for i in x:
            l.append(dic.get(i))
        return(l[::-1])