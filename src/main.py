from Cube import Cube
from UCS import UCS
from Node import Node

def main():
    cube = Cube()
    cube.moves([1,4,2,6,7,3,2])
    cube.printCube()
    initNode = Node(cube=cube, depth=0, h=0)
    astar = UCS(initNode)
    result = astar.run()

    while result.parent:
        result.cube.printCube()
        result = result.parent
    result.cube.printCube()
    
if __name__ == '__main__':
    main()