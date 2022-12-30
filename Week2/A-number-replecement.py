n = int(input())
for i in range(n):
    m = int(input())
    arr = input().split()
    string = input()
    mp = {}
    flg = False
    for i in range(m):
        if arr[i] not in mp:
            mp[arr[i]] = string[i]
        elif arr[i] in mp and string[i] != mp[arr[i]] :
                print("NO")
                flg = True
                break
    if not flg:
        print("YES")
