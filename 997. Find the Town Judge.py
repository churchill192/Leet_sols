class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = None
        trustee = {}
        trusted = {}

        for a,b in trust:
            trustee[a] = trustee.get(a,0)+1
            trusted[b] = trusted.get(b,0)+1

        for i in range(1,n+1):
            if trusted.get(i,0) == n-1 and trustee.get(i,0)==0:
                judge=i
                break
            else:
                judge=-1

       
        return(judge)
        