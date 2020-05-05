class KnightTour:
    def __init__(self,boardsize):
        self.boardsize=boardsize
        self.xMoves=[2,1,-1,-2,-2,-1,1,2]
        self.yMoves=[1,2,2,1,-1,-2,-2,-1]
        self.matrix=[[-1 for x in range(boardsize)] for y in range(boardsize)]

    def solveKnightTour(self):
        # start from x=0,y=0, make it stepcount = 0 instead of -1  for already used
        self.matrix[0][0]=0
        if self.solve(1,0,0):
            self.showSolution()
        else:
            print("Not Feasible Solution found")

    def solve(self,stepCount,x,y):
        # we have visited all the squares of chess return True
        if stepCount == (self.boardsize*self.boardsize):
            return True

        # try all posssible moves(8->len(xMoves) on this stepCount pos to visit square only once
        for i in range(8):
            nextX = x+ self.xMoves[i]
            nextY = y+self.yMoves[i]

            if self.isValid(nextX,nextY):
                self.matrix[nextX][nextY]=stepCount
                # Go to next pos of chess
                if self.solve(stepCount+1,nextX,nextY):
                    return True
                # BackTrack to prev pos and inc xMoves[],yMoves[]
                # try diff pos make this place unvisited first
                self.matrix[nextX][nextY]=-1

        return False

    def isValid(self,x,y):
        if x < 0 or x >= self.boardsize:
            return False
        if y < 0 or y >= self.boardsize:
            return False
        if self.matrix[x][y] > -1:
            return False

        return True

    def showSolution(self):
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                print(self.matrix[i][j],end=" ")
            print()

knight=KnightTour(8)
knight.solveKnightTour()




