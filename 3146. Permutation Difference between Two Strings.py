class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        x = {}
        y = {}

        for i in range(len(s)):
            x[s[i]] = s.index(s[i])
            y[t[i]] = t.index(t[i])

        c=0
        for i in s:
            c += abs(x.get(i)-y.get(i))

        return (c)
        