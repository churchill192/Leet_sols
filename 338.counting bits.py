class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        arr = []
        for i in range(0,n+1):
            arr.append(i)
        
        for i in arr:
            strr=""
            x=bin(i)
            strr+=x
            a=strr.count("1")
            res.append(a)
        
        return res

        