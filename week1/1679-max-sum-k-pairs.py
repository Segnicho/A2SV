class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for i in range(len(command)-1):
            if command[i] == "G":
                res += "G"
            if command[i] == "(" and command[i+1] == "a":
                res += "al"
                i+=3
            if command[i] == "(" and command[i+1] == ")":
                res += "o"
        if command[-1] == "G":
            res += "G"

        return res
