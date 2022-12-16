class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        ordA = ord('a')
        for ch in s:
            if ch.isalnum():
            # if ord(ch) >= ordA and ord(ch) <= ordA+26 and:
                newS+=ch
        n = len(newS)
        if n < 2:
            return True
        for i in range (n//2):
            if newS[i] != newS[(n-1-i)]:
                return False
        return True