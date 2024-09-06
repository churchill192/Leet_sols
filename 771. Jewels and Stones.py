class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x={}
        for i in stones:
            x[i] = stones.count(i)
        c=0
        for i in jewels:
            if i in x:
                c+=(x.get(i))
            
        return(c)

        