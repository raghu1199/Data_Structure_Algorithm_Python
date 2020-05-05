
class MazeProblem:
    def __init__(self,mazeTable):
        self.mazeTable=mazeTable
        self.mazeSize=len(mazeTable)
        self.solutionTable=[[0]*self.mazeSize for x in range(self.mazeSize)]

    def solveMaze(self):
        # start at table[0][0]
        # 0-> Wall 1->Empty cell
        # if solution found -> add to solutionTable[x][y]
        if self.solve(0,0):
            self.showResult()
        else:
            print("No feasible Solution..")

    def solve(self,x,y):
        # if target found here target is at lastPosition of table
        if x == self.mazeSize-1 and y == self.mazeSize-1:
            self.solutionTable[x][y]=1
            return True
        if self.isValid(x,y):

            # add cordinate to Solutionpath
            self.solutionTable[x][y]=1

            # go downword x++
            if self.solve(x+1,y):
                return True
            # can't go downword ->backTrack and go forward y++ --->
            if self.solve(x,y+1):
                return True

            # backward <--
            if self.solve(x,y-1):
                return True
            # at backTrack time add this [x][y] to solution indicating no path
            # always executed when solve() ->false
            self.solutionTable[x][y]=0
        return False

    def isValid(self,x,y):
        if x<0 or x>=self.mazeSize:
            return False
        if y<0 or y>=self.mazeSize:
            return False

        # if wall return false-> backtrack
        if self.mazeTable[x][y]==0:
            return False

        return True

    def showResult(self):
        for i in range(self.mazeSize):
            for j in range(self.mazeSize):
                if self.solutionTable[i][j]==1:
                    print(" S ",end="")
                else:
                    print(" - ",end="")
            print()

    def printMaze(self):

        for i in range(self.mazeSize):
            for j in range(self.mazeSize):
                if self.mazeTable[i][j]==1:
                    print(" - ",end="")
                else:
                    print(" W ",end="")
            print()

mazeTable=[
            [1,1,1,1,0],
            [0,1,0,1,1],
            [1,0,1,1,0],
            [1,0,1,0,0],
            [0,0,1,1,1]
]


m=MazeProblem(mazeTable)
print("MAZE ( - ) represents Empty Space ( W ) represents WALL")
print("WE HAVE TO GO STARTING OF MAZE TO LAST POSITION OF MAZE")
m.printMaze()
print("Solution  S->represents Solution Path...")
print("------------------------------------------")
m.solveMaze()







