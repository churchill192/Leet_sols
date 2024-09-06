class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        x = {}
        for i in strs:
            if ("".join(sorted(i))) not in x:
                x["".join(sorted(i))] = []
                x["".join(sorted(i))].append(i)

            else:
                x["".join(sorted(i))].append(i)



        return((x.values()))
                