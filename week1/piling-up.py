# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    T = int(input())
    def getLargest(block):
        if block[-1] >= block[0]:
            rght = block.pop()
            return rght
        lft = block.pop(0)
        return lft
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        stck= [getLargest(arr)]
        i = 0
        flg = False
        while arr:
            stck.append(getLargest(arr))
            if stck[i] < stck[i+1]:
                print('No')
                flg = True
                break
            i+=1
        if not flg:
            print("Yes")
