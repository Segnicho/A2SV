class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = math.inf
        minInd = -1
        for i, pt in enumerate(points):
            if pt[0] == x or pt[1] == y:
                newDis = abs((pt[0] - x) + (pt[1] - y))
                if newDis < dis:
                    dis = newDis
                    minInd = i
        return minInd
