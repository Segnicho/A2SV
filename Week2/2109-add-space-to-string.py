class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        res = ""
        res += s[:spaces[0]]+" "
        for i in range(n-1):
            res += s[spaces[i]: spaces[i+1]]+" "
        # if n>1:
        res+= s[spaces[-1]:]
        print(res)
        return res
