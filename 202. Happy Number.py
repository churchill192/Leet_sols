class Solution:
    def isHappy(self, n: int) -> bool:
        st = str(n)
        seen = set()
        while st!="1" and st not in seen: # for example n=2 if u keep adding its sqares of digits at somepoint it will come as 2 so its in a cycle so when not in cycle the while loop will break.
            seen.add(st)
            sum = 0
            for i in st:
                sum+=int(i)**2
            st = str(sum)

        if st == "1":
            return(True)
        else:
            return(False)
        