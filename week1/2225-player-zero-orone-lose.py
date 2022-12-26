class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[],[]]
        losers = set()
        lcount = {}
        for match in matches:
            lcount[str(match[1])] = lcount.get(str(match[1]), 0)+1
        for ky in lcount.keys():
            if lcount[ky] == 1:
                res[1].append(int(ky))
        for match in matches:
            losers.add(match[1])
        for match in matches:
            losers.add(match[1])
        visited = set()
        for match in matches:
            if match[0] not in losers and  match[0] not in visited :
                res[0].append(match[0])
            visited.add(match[0])
        res[0].sort()
        res[1].sort()
        return res
