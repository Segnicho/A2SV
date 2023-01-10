class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        res = ""
        def multiply(num1, num2):
            return num1*num2
        arr1 = num1.split("+")
        arr2 = num2.split("+")
        arr1[0] = eval(arr1[0])
        real = arr1[1][:-1] 
        arr1[1] = int(real)

        arr2[0] = eval(arr2[0])
        real = arr2[1][:-1] 
        arr2[1] = int(real)
        
        realp = multiply(arr1[0], arr2[0]) - multiply(arr1[1], arr2[1])
        
        imap = multiply(arr1[0], arr2[1]) + multiply(arr1[1], arr2[0])

        res+=str(realp)+"+"+str(imap)+"i"
        return res

        
        
