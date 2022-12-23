class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp = self.Mapr()
        newS = ''
        if len(s)<3:
            for char in s:
                newS += mp[char]
            return newS 
        i = 0
        n = len(s)
        while i < n-2:
            if s[i+2] == '#':
                newS += mp[s[i:i+3]]
                i+=3
            else:
                newS += mp[s[i]]
                i+=1
        while i < len(s):
            newS +=  mp[s[i]]
            i+=1
        return newS
        
    def Mapr(self):
        mp = {}
        ordA = ord('a')
        for i in range(9):
            mp[str(i+1)] = chr((ordA))
            ordA += 1
        ordJ = ord('j')
        for i  in range(10, 27):
            mp[str(i)+"#"] = chr((ordJ))
            ordJ += 1
        return mp
