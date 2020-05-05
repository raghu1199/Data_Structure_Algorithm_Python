class Coloring_Problem:
    def __init__(self, numofVertices, numofColors, graphMatrix):
        self.numofVertices = numofVertices
        self.numofColors = numofColors
        self.colors = [0] * numofVertices
        self.graphMatrix = graphMatrix

    def solveColoring(self):
        if self.solve(0):
            self.showresult()
        else:
            print("No Feasible Solution..")

    def solve(self,nodeIndex):
        if nodeIndex==self.numofVertices:
            return True
        for colorIndex in range(1,self.numofColors+1):
            print(f"check Valid ?colorIndex:{colorIndex} nodeIndex:{nodeIndex}")
            if self.iscolorValid(nodeIndex,colorIndex):
                print(f"Valid colorIndex:{colorIndex} node:{nodeIndex}",end=" ")
                self.colors[nodeIndex]=colorIndex
                print("colors:",self.colors)
                if self.solve(nodeIndex+1):
                    return True

                # Backtrack
        return False

    def iscolorValid(self,nodeIndex,colorIndex):
        for i in range(self.numofVertices):
            if self.graphMatrix[nodeIndex][i]==1 and colorIndex == self.colors[i]:
                return False

        return True

    def showresult(self):
        for i in range(self.numofVertices):
            print(f"Node {i} has colorIndex:{self.colors[i]}")

gm=[
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [1,1,1,0,1],
    [0,0,0,1,0]
]
cp=Coloring_Problem(5,3,gm)
cp.solveColoring()




