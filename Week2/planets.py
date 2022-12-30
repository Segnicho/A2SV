n = int(input())
from collections import Counter

for i in range(n):
    minC = 0
    n, c = input().split()
    c = int(c)
    arr = list(map(int, input().split()))
    cnt = Counter(arr)
    for ky, val in cnt.items():
        if val < c:
            minC += val
        else:
            minC += c
    print(minC)




