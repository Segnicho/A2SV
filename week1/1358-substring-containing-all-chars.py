class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        sMap = {'a':0, 'b':0, 'c':0}
        cnt = lptr = rptr = 0
        for rptr in range (len(s)):
            sMap[s[rptr]] = sMap[s[rptr]] + 1
            while sMap['a'] > 0  and sMap['b'] >0 and sMap['c'] > 0:
                cnt+=len(s)-rptr
                sMap[s[lptr]] = sMap[s[lptr]] - 1
                lptr+=1
        return cnt
