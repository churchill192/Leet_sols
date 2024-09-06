class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        x = (num ** 0.5) * 10
        if x % 10 == 0:
            return True
        else:
            return False


