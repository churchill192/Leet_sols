class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split())) 
        #return " ".join(s.split()[::-1])
        
                    