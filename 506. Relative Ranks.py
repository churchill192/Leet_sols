class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sorted_score = sorted(score, reverse = True)
        model_dict = {}
        res = []

        for i in range(len(sorted_score)):

            if i == 0:
                model_dict[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                model_dict[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                model_dict[sorted_score[i]] = "Bronze Medal"
            
            else:
                model_dict[sorted_score[i]] = str(i+1)
        
        for s in score:
            res.append(model_dict[s])
        
        return res