class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        can = True
        five_count = 0
        ten_count = 0
        for i in range(len(bills)):
            if  bills[i]==5:
                five_count +=1

            else:
                if bills[i] == 10:
                    if five_count>0:
                        five_count -=1
                        ten_count +=1
                    else:
                        can=False
                        break

                if bills[i] == 20:
                    if five_count>0 and ten_count>0:
                        five_count -=1
                        ten_count-=1

                    elif five_count>=3:
                        five_count -=3
                    else:
                        can=False
                        break
        return(can)
