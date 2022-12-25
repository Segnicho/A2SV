class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        worder = {}
        for i, ch in enumerate(order):
            worder[ch] = i
        edg = False
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if worder[word1[j]] > worder[word2[j]]:
                    return False
                if worder[word1[j]] < worder[word2[j]]:
                    edg  = True
                    break
            if not edg and len(word1) > len(word2):
                return False
        return True
