from Cube import Cube

class Node(object):
    def __init__(self, cube: Cube, depth: int, h: int):
        self.cube = cube
        self.depth = depth
        self.h = h
        self.parent = None
        self.move = None
        
    def expand(self):
        children = []
        for num in range(1,13):
            newCube = self.cube.clone()
            newCube.move(num)
            newNode = Node(cube=newCube, depth=self.depth + 1, h=0)
            newNode.parent = self
            newNode.move = num
            if not self.parent or newNode != self.parent:
                children.append(newNode)
        
        return children

    def __cmp__(self, other):
        if (self.depth + self.h < other.depth + other.h):
            return -1
        elif (self.depth + self.h == other.depth + other.h):
            return 0
        else:
            return 1

    def __lt__(self, other):
        return (self.depth + self.h < other.depth + other.h)

    def __eq__(self, other):
        return (self.depth + self.h == other.depth + other.h)

    def __gt__(self, other):
        return (self.depth + self.h > other.depth + other.h)
