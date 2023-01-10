class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [[0,1],[1,0], [1, 1],[0,-1], [-1,0],[-1,-1], [-1,1], [1,-1]]
        start = king
        res = []
        for i, j in dirs:
            si = king[0]
            sj = king[1]
            while 0 <= si <= 7 and 0 <= sj <= 7:
                 si += i
                 sj+=j
                 if [si, sj] in queens:
                     res.append([si, sj])
                     break
        return res
