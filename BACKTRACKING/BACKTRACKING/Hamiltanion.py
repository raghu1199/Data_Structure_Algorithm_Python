
class Hamiltanion_Problem:
    def __init__(self,adjacencyMatrix):
        self.numofVertex=len(adjacencyMatrix)
        self.hamiltonPath=[None]*self.numofVertex
        self.adjacencyMatrix=adjacencyMatrix

    def hamiltoncycle(self):
        # give 0th index vertice
        self.hamiltonPath[0]=0
        # give position= 1 to start
        if not self.findSolution(1):
            print("No feasible solution..")
        else:
            self.showHamiltonPath()

    def findSolution(self,position):
        # base case end of position(column) end is connected to start
        # [c][a] -> c lastindex a->first index of first column
        if position == self.numofVertex:
            x= self.hamiltonPath[position-1]
            y= self.hamiltonPath[0]
            if self.adjacencyMatrix[x][y] == 1:
                return True
            else:
                return False

        # goes like a->b Yes a->c No
        # b->b b->c
        for vertexIndex in range(self.numofVertex):
            if self.isFeasible(vertexIndex,position):
                self.hamiltonPath[position] = vertexIndex
                if self.findSolution(position+1):
                    return True

                # backtrack and increment to next vertex and go to prev column position
        return False

    def isFeasible(self,vertexIndex,position):
        # first criteria: check wether connected or not a<->b,a->c:
        x= self.hamiltonPath[position-1]
        y=vertexIndex
        if self.adjacencyMatrix[x][y] == 0:
            return False

        # second criteria already in hamiltonPath?
        for j in range(position):
            if self.hamiltonPath[j]== vertexIndex:
                return False

        return True

    def showHamiltonPath(self):
        print("HamiltonCycle Exist:")
        for j in range(self.numofVertex):
            print(self.hamiltonPath[j])
        print(self.hamiltonPath[0])


h= Hamiltanion_Problem([ [0,1,0],
                         [1,0,1],
                         [1,1,0],
                        ])
h.hamiltoncycle()



