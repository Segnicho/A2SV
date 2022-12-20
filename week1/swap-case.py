def swap_case(s):
    newL = []
    for l in s:
        ltr = l.isalpha()
        if ltr:
            if l.islower():
                upr = l.upper()
                newL.append(upr)
            else:
                lwr = l.lower()
                newL.append(lwr)
        else:
            newL.append(l)
    return "".join(newL)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
