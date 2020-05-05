class QueensProblem:
    def __init__(self,numofQueens):
        self.numofQueens=numofQueens
        self.chessTable=[[None for i in range(numofQueens)] for j in range(numofQueens)]

    def solveQueenProble(self):
        # column index ->0
        if self.solve(0):
            self.printQueens()
        else:
            print("There is No solution..")

    def solve(self,colIndex):
        if colIndex == self.numofQueens:
            return True

        for rowIndex in range(self.numofQueens):

            if self.isPlaceValid(rowIndex,colIndex):
                self.chessTable[rowIndex][colIndex] = 1

                if self.solve(colIndex+1):
                    return True
                # we have to do backtrack come back to prev col beacuase colIndex+1 has returned False
                # we just have to make prev place 0 to remove queen and try next row
                self.chessTable[rowIndex][colIndex]=0

        # if all row is traversed and find no any true -> need Backtrack terminate solve(colIndex+1)
        return False

    def isPlaceValid(self,rowIndex,colIndex):
        # same row check
        for i in range(colIndex):
            if self.chessTable[rowIndex][i] == 1:
                return False

        # for bottom right to top left diogonal check go current row to prev row and current col to prev col
        # [r2][c3],[r1][c2]
        j=colIndex
        for i in range(rowIndex,-1,-1):
            if j<0:
                break
            if self.chessTable[i][j] == 1:
                return False
            j=j-1

        # top right to bottom left
        j=colIndex
        for i in range(rowIndex,len(self.chessTable)):
            if j<0:
                break
            if self.chessTable[i][j] == 1:
                return False
            j=j-1

        return True

    def printQueens(self):
        for i in range(self.numofQueens):
            for j in range(self.numofQueens):
                if self.chessTable[i][j] == 1:
                    print(" Q ",end="")
                else:
                    print(" - ",end="")
            print("\n")

qns=QueensProblem(4)
qns.solveQueenProble()
print("For 8 Queens:")
qns=QueensProblem(8)
qns.solveQueenProble()



