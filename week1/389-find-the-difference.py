class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}
        for element in t:
            tMap[element] = tMap.get(element, 0)+1
        for element in s:
            sMap[element] = sMap.get(element, 0)+1
        for el in tMap.keys():
            if el not in sMap.keys():
                return el
            if tMap[el] != sMap[el]:
                return el
