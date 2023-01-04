class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split(" ")
        print(arr)
        res = []
        max_ = 0
        for el in arr:
            max_ = max(len(el), max_)
        for i in range(max_):
            temp = ""
            for j in range(len(arr)):
                if i >= len(arr[j]) :
                    temp += " "
                else:
                    temp += arr[j][i]
            res.append(temp)
        for i in range(len(res)):
            temp = list(res[i])
            while temp[-1] == " ":
                print("here")
                temp.pop()
            res[i] = "".join(temp)
        return res
