class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        list1 = list(s)

        while l<r:
            if list1[l] in vowels and list1[r] in vowels:
                
                list1[l],list1[r] = list1[r],list1[l]
                

                l+=1
                r-=1

            if list1[l] not in vowels:
                l+=1
            if list1[r] not in vowels:
                r-=1
        s = "".join(list1)
        
        return s

        