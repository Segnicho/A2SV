if __name__ == '__main__':
    n = int(input())
    ls = tuple(map(int, input().split()))
    print(hash(ls))
