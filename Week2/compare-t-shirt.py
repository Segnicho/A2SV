n = int(input())
vald = ["S", "M", "L"]
def calcTShirtSize(tshirt):
    size = 1
    for letter in tshirt:
        if letter == "M":
            return 0
        if letter not in vald:
            size += 2
        if letter == vald[0]:
            size*=-1
        if letter == vald[2]:
            size *= 1
    return size
for i in range(n):
    sizes = input().split()
    size1 = calcTShirtSize(sizes[0])
    size2 = calcTShirtSize(sizes[1])
    # print(size1, size2)
    if size1 > size2:
        print(">")
        continue
    if size2 >size1 :
        print("<")
        continue
    else:
        print("=")
        continue
