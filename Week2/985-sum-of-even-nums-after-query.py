class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        def isEven(num):
            return num%2 ==0
        def countEven(arr):
            temp = 0
            for num in arr:
                if num % 2 ==0:
                    temp += num
            return temp
        for items in queries:

            val, index = items[0], items[1]
            curr = nums[index] 
            newVal = curr + val
            temp = 0
            nums[index] = newVal
            # if isEven(nums[-1]):
            if not res:
                x = countEven(nums)
                res.append(x)
            else:
                # curr = nums[index]
                last = res[-1]
                if isEven(curr):
                    if not isEven(newVal):
                        last -= curr
                    else:
                        last-=curr 
                        last+=newVal
                else:
                    if isEven(newVal):
                        last+=newVal
                res.append(last)

        return res
