from Cube import Cube

def main():
    cube = Cube()
    cube.printCube()

    for i in range(6):
        cube.rotateRightCounterCW()
        cube.rotateBottomCW()
        cube.rotateRightCW()
        cube.rotateBottomCounterCW()
        cube.printCube()
        print('_________________________________')

    print(cube.isSolved())
if __name__ == '__main__':
    main()