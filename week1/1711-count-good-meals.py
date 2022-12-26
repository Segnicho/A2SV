class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = {2**i for i in range(21)}
        mod = 10**9 +7
        res = 0

        ctr = Counter(deliciousness)
        
        for d, n in ctr.items():
            if d in powers:
                res += n*(n-1)
            for p in powers:
                k = p-d
                if k != d and k in ctr:
                    res += ctr[k]*n
        return res//2%(mod)
