class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        onesIdx = []
        for i, el in enumerate(boxes):
            if el =="1":
                onesIdx.append(i)
        res = [0]*len(boxes)
        for i, s in enumerate(boxes):
            temp = 0
            for ind in onesIdx:
                if i == ind:
                    continue
                temp += abs(ind - i)     
            res[i] = temp
        return res
        
