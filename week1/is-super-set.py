def isStrictSubset():
    A = set(map(int, input().split()))
    n = int(input())
    newS = []
    for i in range(n):
        ls = set(map(int, input().split()))
        if not A.issuperset(ls):
            return False
    return True
print(isStrictSubset())

        
