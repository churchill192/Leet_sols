class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        x = list(s)
        l = 0
        r = len(s)-1

        while l<r:
            if x[l].isalpha() and x[r].isalpha():
                x[l],x[r] = x[r],x[l]
                l+=1
                r-=1
            elif not x[l].isalpha():
                l+=1
            elif not x[r].isalpha():
                r-=1
            #l+=1
            #r-=1
        
        s="".join(x)
        return s
        