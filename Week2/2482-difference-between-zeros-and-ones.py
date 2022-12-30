class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(grid[0]) for _ in range(len(grid))]
        rw0 = [0] * len(grid)
        rw1 = [0]* len(grid) 
        col0 = [0]* len(grid[0])
        col1 = [0] * len(grid[0])
        for i in range(len(grid)):
            cnt0 = 0
            cnt1 = 0
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    cnt0+=1
                else:
                    cnt1+=1
            rw0[i] = cnt0
            rw1[i] = cnt1
        for i in range(len(grid[0])):
            cnt0 = 0
            cnt1 = 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    cnt0+=1
                else:
                    cnt1+=1
            col0[i] = cnt0
            col1[i] = cnt1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = rw1[i] + col1[j] - rw0[i] - col0[j]
        return res
