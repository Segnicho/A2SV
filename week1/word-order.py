# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
l = []
n = eval(input())
for i in range(n):
    wrd = input()
    l.append(wrd)
x = {}
for word in l:
    x[word] = x.get(word, 0)+1
print(len(x))
print(*x.values())

