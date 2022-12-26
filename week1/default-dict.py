# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
dkt = defaultdict(list)
if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)
    # print(dkt)
    for i in range(n):
        string  = input()
        dkt[string].append(i+1)
    B = []
    for i in range(m):
        string  = input()
        B.append(string)
    for ltr in B:
        if ltr in dkt:
            for l in dkt[ltr]:
                print(l, end=" ")
            print()
        else:
            print(-1)
