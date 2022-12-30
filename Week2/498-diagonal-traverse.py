class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        res = []
        reverse = False

        for i in range(n):
            # for j in range(m):
            row = i
            col = 0
            temp = [mat[row][col]]    
            while 0<= row-1 < n and 0 <= col+1 < m:
                temp.append(mat[row-1][col+1])
                row-=1
                col+=1
            if reverse:
                temp.reverse()
            reverse = not reverse
            res.append(temp)

        # return
        for i in range(1, m):
                row = n-1
                col = i
                temp = [mat[row][col]]    
                while 0 <= row-1 < n and 0 <= col+1 < m:
                    temp.append(mat[row-1][col+1])
                    row-=1
                    col+=1
                if reverse:
                    temp.reverse()
                reverse = not reverse
                res.append(temp)
        ans = []
        for i in range(len(res)):
            for j in range(len(res[i])):
                ans.append(res[i][j])
        return ans
