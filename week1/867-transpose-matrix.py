class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
            m = len(matrix)
            n = len(matrix[0])
            res = [[0]*m for i in range (n)]
            # res2 = [[0]*m]*n
            for i in range(len(res)):
                for j in range(len(res[0])):
                    res[i][j] = matrix[j][i]
            # return zip(*matrix)
            return res

