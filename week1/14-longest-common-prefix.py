class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]):
                    return res
                if curr != strs[j][i]:
                    return res
            res+=curr
        return res
