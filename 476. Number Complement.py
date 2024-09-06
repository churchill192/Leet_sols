class Solution:
    def findComplement(self, num: int) -> int:
        b = str(bin(num))
        c = ""
        for i in b:
            if i == "0":
                c+="1"
            else:
                c+="0"
        bina = c[2:]

        return(int(bina,2))
        