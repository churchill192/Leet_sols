class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list1 = list(s)
        i = 0

        while i<len(s):
            
            l = i
            r = min(i+k-1,len(s)-1)
            while l<r:
                list1[l],list1[r] = list1[r],list1[l]
                #i+=2
                l+=1
                r-=1
                
            i+=2*k
                   
            





        s = "".join(list1)
        return(s)
                