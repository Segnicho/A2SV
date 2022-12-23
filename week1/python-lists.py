if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        A = list(map(str, input().split()))
        if len(A) == 1:
            if A[0] == "print":
                print(arr)
            if A[0] == "sort":
                arr.sort()
            if A[0] == "pop" :
                arr.pop()
            if A[0] == "reverse":
                arr.reverse()
        elif len(A) == 2:
            if A[0] == "remove":
                arr.remove(eval(A[1]))
            if A[0] == "append":
                arr.append(eval(A[1]))
        else:
            arr.insert(eval(A[1]), eval(A[2]))
    
                
            
