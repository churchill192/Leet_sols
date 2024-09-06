class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        count = 0
        string = str(num) #"240"
        for i in range(len(string)-k+1):

            c = int(string[i:i+k])
            try:
                if num%c==0:
                    count+=1
            except:
                pass

        return(count)
        