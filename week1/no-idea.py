# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    nm = list(map(int, input().split()))
    arr = list(map(int, input().split()))  
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    happiness = 0
    mp = {}
    for num in arr:
        mp[num] = mp.get(num,0)+1
    for num in A:
        happiness += mp.get(num, 0)
    for num in B:
        happiness -= mp.get(num, 0)
    print(happiness)
    
