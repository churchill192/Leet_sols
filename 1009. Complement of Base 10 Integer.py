class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        b = str(bin(n))
        c = ""
        for i in b:
            if i == "0":
                c+="1"
            else:
                c+="0"
        bina = c[2:]

        return(int(bina,2))
        
        