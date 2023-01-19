from Node import Node
from heapq import *
from Cube import Cube

class UCS(object):
    def __init__(self, initNode: Node):
        self.initNode = initNode
        self.heap = []

    def run(self):
        children = self.initNode.expand()
        for child in children:
            child.h = self.h(child)
            heappush(self.heap, child)

        while len(self.heap) != 0:
            chosen = heappop(self.heap)
            if chosen.cube.isSolved():
                return chosen

            chosenChildren = chosen.expand()
            for child in chosenChildren:
                child.h = self.h(child)
                heappush(self.heap, child)

    def h(self, node: Node):
        counter = 0
        # solvedCube = Cube()
        # cube = node.cube
        # for i in range(len(cube.top)):
        #     for j in range(len(cube.top[i])):
        #         if cube.top[i][j] != solvedCube.top[i][j]:
        #             counter += cube.top[i][j]
        return counter

