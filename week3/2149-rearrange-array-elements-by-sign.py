class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        negs = []
        res = []
        for index, num in enumerate(nums):
            if num > 0:
                pos.append(num)
            else:
                negs.append(num)
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(negs[i])
        return res
