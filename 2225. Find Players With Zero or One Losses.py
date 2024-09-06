class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # winner = []
        # loser = []
        # winner_res = []
        # loser_res = []
        # final_res = []

        # w = {}
        # l = {}
        # #s[matches[0][0]] = matches[0][0]

        # for i in range(len(matches)):
        #     if matches[i][0] not in winner:
        #         winner.append(matches[i][0])
        #         w[matches[i][0]] = 1
        #     else:
        #         w[matches[i][0]] +=1
            
            
        # #print(w)

        # for i in range(len(matches)):
        #     if matches[i][1] not in loser:
        #         loser.append(matches[i][1])
        #         l[matches[i][1]] = 1
        #     else:
        #         l[matches[i][1]] +=1
        # #print(l)


        # for key in w.keys():
        #     if key not in l.keys():
        #         winner_res.append(key)
        # #print(winner_res)
        # final_res.append(sorted(winner_res))

        # for key,value in l.items():
        #     if value == 1:
        #         loser_res.append(key)
        # #print(loser_res)
        # final_res.append(sorted(loser_res))

        # return(final_res)


        loser_count = {}
        winner_count = set()
        final_res = []

        for winner, loser in matches:
            winner_count.add(winner)

            if loser in loser_count:
                loser_count[loser] += 1
            else:
                loser_count[loser] = 1

            if loser in winner_count:
                winner_count.discard(loser)

        winner_res = []
        loser_res = []
        for i in winner_count:
            if i not in loser_count:
                winner_res.append(i)


        for key,value in loser_count.items():
            if value == 1:
                loser_res.append(key)

        final_res.append(sorted(winner_res))
        final_res.append(sorted(loser_res))
        return(final_res)
                        