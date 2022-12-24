# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = input().split()
    st = set(map(str, input().split()))
    b = input().split()
    nxt = set(map(str, input().split()))
    res = st.difference(nxt)
    print(len(res))
