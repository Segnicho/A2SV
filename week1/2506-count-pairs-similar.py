class Solution:
    def similarPairs(self, words: List[str]) -> int:
        vistd = set()
        cnt = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if self.isSimilar(words[i], words[j]):
                    cnt += 1
        return cnt

    def isSimilar(self,str1, str2):
        mp1 = {}
        mp2 = {}
        for ch in str1:
            mp1[ch] = mp1.get(ch, 0) + 1
        for ch in str2:
            mp2[ch] = mp2.get(ch, 0) + 1
        return mp1.keys() == mp2.keys()
                
