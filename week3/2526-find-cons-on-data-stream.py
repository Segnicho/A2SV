class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.mp = {}
        self.size = 0      
        self.arr = []
    def consec(self, num: int) -> bool:
        self.arr.append(num)
        self.mp[num] = self.mp.get(num, 0) + 1
        self.size+=1
        # print(self.size, self.k)
        if self.size < self.k:
            return False
        if self.size == self.k:
            if self.mp == {self.value:self.k}:
                return True
        else:
            self.mp[self.arr[self.size-self.k-1]] = self.mp[self.arr[self.size-self.k-1]] - 1
            if self.mp[self.arr[self.size-self.k-1]] == 0:
                del self.mp[self.arr[self.size-self.k-1]]
            if self.mp == {self.value:self.k}:
                return True
            # self.mp[self.arr[self.size-self.k]] = self.mp[self.arr[self.size-self.k]] - 1
            # if self.mp[self.arr[self.size-self.k]] == 0:
            #     del self.mp[self.arr[self.size-self.k]]
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
