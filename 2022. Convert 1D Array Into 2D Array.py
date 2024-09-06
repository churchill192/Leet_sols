class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original)!= m*n:
            return None

        x = []
        for i in range(m):
            start = i*n
            end = start+n
            x.append(original[start:end])
        return x

        