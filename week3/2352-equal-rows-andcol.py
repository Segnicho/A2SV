class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        zped = [list(cols) for cols in zip(*grid)]
        # print(zped)
        cnt = 0
        for row in grid:
            for col in zped:
                if row == col:
                    cnt+=1
        return cnt
