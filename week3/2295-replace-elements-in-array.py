class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = defaultdict()
        for i, num in enumerate( nums):
            mp[str(num)] = i
        for num, repl in operations:
            ind = mp[str(num)]
            nums[(ind)] = repl
            mp[str(repl)] = ind
        return nums

