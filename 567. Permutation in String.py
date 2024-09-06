class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1 = "".join(sorted(s1))
        
        
        
        length = len(s1) #2- [0,1]
        l = 0
        r = len(s1)-1
        bl = False
        for i in range(0,len(s2)-length+1):
            x = "".join(sorted(s2[l:r+1]))
            if s1 == x:
                bl=True
                break
            l+=1
            r+=1
        return(bl)

        