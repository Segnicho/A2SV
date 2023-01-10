class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:     
        mp = {"X":0,
            "O":0,
            " ":0
        }
        for row in board:
            for col in row:
                mp[col]+=1
        del mp[" "]
        if not mp["X"] == mp["O"] and not mp["X"] == mp["O"] +1:
            return False
        
        zped = []
        # zped = [str(rws) for rws in zip(*board)]
        for i in range(3):
            temp = ""
            for j in range(3):
                temp+=board[j][i]
            zped.append(temp)
        print(zped)
        def illegal(board):
            xs = "XXX"
            os = "OOO"
            xsb = False
            osb = False
            # zped = (list(rws) for rws in zip(*board))
            rdiag = ""
            ldiag = ""
            rdiag += board[0][0]+board[1][1]+board[2][2]
            ldiag += board[0][2]+board[1][1]+board[2][0]
            if rdiag == xs or ldiag == xs:
                xsb = True
            if rdiag == os or ldiag == os:
                osb = True
            for rw in board:
                if rw == xs:
                    xsb = True
                if rw == os:
                    osb = True
            for col in zped:
                if col == xs:
                    xsb = True
                if col == os:
                    osb = True 
            if osb and xsb:
                return True  
            if xsb and mp["X"] - mp["O"] != 1:
                return True 
            if osb and mp["X"] != mp["O"]:
                return True
            return False
        if illegal(board):
            return False
        return True


