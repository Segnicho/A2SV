if __name__ == '__main__':
    n = int(input())
    arr = list(map(str, input().split()))
    mp = {}
    for num in arr:
        mp[(num)] = mp.get((num), 0) + 1
    for ky in mp.keys():
        if mp[ky] == 1:
            print(int(ky))
            break
    # print(mp)
