class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # res = [0]*len(nums)
        ls = []
        eq = []
        gre = []
        for num in nums:
            if num<pivot:
                ls.append(num)
            if num > pivot:
                gre.append(num)
            if num == pivot:
                eq.append(num)
        return ls+eq+gre
