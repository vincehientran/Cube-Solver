import numpy as np

class bcolors:
    BLUE = '\033[1;34m'
    CYAN = '\033[1;36m'
    GREEN = '\033[1;32m'
    RED = '\033[1;31m'
    YELLOW = '\033[1;33m'
    MAGENTA = '\033[1;35m'

    BLUE_HIGHLIGHT = '\033[0;34;44m'
    CYAN_HIGHLIGHT = '\033[0;36;46m'
    GREEN_HIGHLIGHT = '\033[0;32;42m'
    RED_HIGHLIGHT = '\033[0;31;41m'
    YELLOW_HIGHLIGHT = '\033[0;33;43m'
    MAGENTA_HIGHLIGHT = '\033[0;35;45m'

    BLUE_UNDERLINE = '\033[4;34m'
    CYAN_UNDERLINE = '\033[4;36m'
    GREEN_UNDERLINE = '\033[4;32m'
    RED_UNDERLINE = '\033[4;31m'
    YELLOW_UNDERLINE = '\033[4;33m'
    MAGENTA_UNDERLINE = '\033[4;35m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\033[0;37;47m'

class Cube(object):
    def __init__(self, state=None):
        if not state:
            self.top = [[1 for _ in range(3)] for _ in range(3)]
            self.bottom = [[2 for _ in range(3)] for _ in range(3)]
            self.front = [[3 for _ in range(3)] for _ in range(3)]
            self.back = [[4 for _ in range(3)] for _ in range(3)]
            self.left = [[5 for _ in range(3)] for _ in range(3)]
            self.right = [[6 for _ in range(3)] for _ in range(3)]
        else:
            self.top = state[0]
            self.bottom = state[1]
            self.front = state[2]
            self.back = state[3]
            self.left = state[4]
            self.right = state[5]
    
    def rotateTopCW(self):
        self.faceRotateCW(self.top)

        frontRow = self.front[0]
        self.front[0] = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = frontRow

    def rotateTopCounterCW(self):
        self.faceRotateCounterCW(self.top)

        frontRow = self.front[0]
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = self.right[0]
        self.right[0] = frontRow

    def rotateBottomCW(self):
        self.faceRotateCW(self.bottom)

        frontRow = self.front[2]
        self.front[2] = self.left[2]
        self.left[2] = self.back[2]
        self.back[2] = self.right[2]
        self.right[2] = frontRow

    def rotateBottomCounterCW(self):
        self.faceRotateCounterCW(self.bottom)

        frontRow = self.front[2]
        self.front[2] = self.right[2]
        self.right[2] = self.back[2]
        self.back[2] = self.left[2]
        self.left[2] = frontRow

    def rotateFrontCW(self):
        self.faceRotateCW(self.front)

        topRow = self.top[2]
        self.top[2] = [row[2] for row in self.left][::-1]
        self.left = np.array(self.left)
        self.left[:,2] = self.bottom[0]
        self.left = np.ndarray.tolist(self.left)
        self.bottom[0] = [row[0] for row in self.right][::-1]
        self.right = np.array(self.right)
        self.right[:,0] = topRow
        self.right = np.ndarray.tolist(self.right)

    def rotateFrontCounterCW(self):
        self.faceRotateCounterCW(self.front)

        topRow = self.top[2]
        self.top[2] = [row[0] for row in self.right]
        self.right = np.array(self.right)
        self.right[:,0] = self.bottom[0][::-1]
        self.right = np.ndarray.tolist(self.right)
        self.bottom[0] = [row[2] for row in self.left]
        self.left = np.array(self.left)
        self.left[:,2] = topRow[::-1]
        self.left = np.ndarray.tolist(self.left)

    def rotateBackCW(self):
        self.faceRotateCW(self.back)

        topRow = self.top[0]
        self.top[0] = [row[2] for row in self.right]
        self.right = np.array(self.right)
        self.right[:,2] = self.bottom[2][::-1]
        self.right = np.ndarray.tolist(self.right)
        self.bottom[2] = [row[0] for row in self.left]
        self.left = np.array(self.left)
        self.left[:,0] = topRow[::-1]
        self.left = np.ndarray.tolist(self.left)

    def rotateBackCounterCW(self):
        self.faceRotateCounterCW(self.back)

        topRow = self.top[0]
        self.top[0] = [row[0] for row in self.left][::-1]
        self.left = np.array(self.left)
        self.left[:,0] = self.bottom[2]
        self.left = np.ndarray.tolist(self.left)
        self.bottom[2] = [row[2] for row in self.right][::-1]
        self.right = np.array(self.right)
        self.right[:,2] = topRow
        self.right = np.ndarray.tolist(self.right)

    def rotateLeftCW(self):
        self.faceRotateCW(self.left)

        topRow = [row[0] for row in self.top]
        self.top = np.array(self.top)
        self.top[:,0] = [row[2] for row in self.back][::-1]
        self.top = np.ndarray.tolist(self.top)

        self.back = np.array(self.back)
        self.back[:,2] = [row[0] for row in self.bottom][::-1]
        self.back = np.ndarray.tolist(self.back)

        self.bottom = np.array(self.bottom)
        self.bottom[:,0] = [row[0] for row in self.front]
        self.bottom = np.ndarray.tolist(self.bottom)

        self.front = np.array(self.front)
        self.front[:,0] = topRow
        self.front = np.ndarray.tolist(self.front)

    def rotateLeftCounterCW(self):
        self.faceRotateCounterCW(self.left)

        topRow = [row[0] for row in self.top]
        self.top = np.array(self.top)
        self.top[:,0] = [row[0] for row in self.front]
        self.top = np.ndarray.tolist(self.top)

        self.front = np.array(self.front)
        self.front[:,0] = [row[0] for row in self.bottom]
        self.front = np.ndarray.tolist(self.front)

        self.bottom = np.array(self.bottom)
        self.bottom[:,0] = [row[2] for row in self.back][::-1]
        self.bottom = np.ndarray.tolist(self.bottom)

        self.back = np.array(self.back)
        self.back[:,2] = topRow[::-1]
        self.back = np.ndarray.tolist(self.back)

    def rotateRightCW(self):
        self.faceRotateCW(self.right)

        topRow = [row[2] for row in self.top]
        self.top = np.array(self.top)
        self.top[:,2] = [row[2] for row in self.front]
        self.top = np.ndarray.tolist(self.top)

        self.front = np.array(self.front)
        self.front[:,2] = [row[2] for row in self.bottom]
        self.front = np.ndarray.tolist(self.front)

        self.bottom = np.array(self.bottom)
        self.bottom[:,2] = [row[0] for row in self.back][::-1]
        self.bottom = np.ndarray.tolist(self.bottom)

        self.back = np.array(self.back)
        self.back[:,0] = topRow[::-1]
        self.back = np.ndarray.tolist(self.back)

    def rotateRightCounterCW(self):
        self.faceRotateCounterCW(self.right)

        topRow = [row[2] for row in self.top]
        self.top = np.array(self.top)
        self.top[:,2] = [row[0] for row in self.back][::-1]
        self.top = np.ndarray.tolist(self.top)

        self.back = np.array(self.back)
        self.back[:,0] = [row[2] for row in self.bottom][::-1]
        self.back = np.ndarray.tolist(self.back)

        self.bottom = np.array(self.bottom)
        self.bottom[:,2] = [row[2] for row in self.front]
        self.bottom = np.ndarray.tolist(self.bottom)

        self.front = np.array(self.front)
        self.front[:,2] = topRow
        self.front = np.ndarray.tolist(self.front)

    def faceRotateCW(self, face):
        topLeft = face[0][0]
        face[0][0] = face[2][0]
        face[2][0] = face[2][2]
        face[2][2] = face[0][2]
        face[0][2] = topLeft

        topMiddle = face[0][1]
        face[0][1] = face[1][0]
        face[1][0] = face[2][1]
        face[2][1] = face[1][2]
        face[1][2] = topMiddle

    def faceRotateCounterCW(self, face):
        topLeft = face[0][0]
        face[0][0] = face[0][2]
        face[0][2] = face[2][2]
        face[2][2] = face[2][0]
        face[2][0] = topLeft

        topMiddle = face[0][1]
        face[0][1] = face[1][2]
        face[1][2] = face[2][1]
        face[2][1] = face[1][0]
        face[1][0] = topMiddle

    def convertMoveNumToStr(self, num):
        d = {1:'U', 2:'U\'', 3:'D', 4:'D\'',
        5:'F', 6:'F\'', 7:'B', 8:'B\'',
        9:'L', 10:'L\'', 11:'R', 12:'R\''}
        return d[num]

    def convertMoveStrToNum(self, string):
        d = {'U':1, 'U\'':2, 'D':3, 'D\'':4,
        'F':5, 'F\'':6, 'B':7, 'B\'':8,
        'L':9, 'L\'':10, 'R':11, 'R\'':12}
        return d[string]

    def isSolved(self):
        solved = True
        solved &= self.top == [[1 for _ in range(3)] for _ in range(3)]
        solved &= self.bottom == [[2 for _ in range(3)] for _ in range(3)]
        solved &= self.front == [[3 for _ in range(3)] for _ in range(3)]
        solved &= self.back == [[4 for _ in range(3)] for _ in range(3)]
        solved &= self.left == [[5 for _ in range(3)] for _ in range(3)]
        solved &= self.right == [[6 for _ in range(3)] for _ in range(3)]
        return solved

    def stringColor(self, num):
        if num == 1:
            return bcolors.HIGHLIGHT + str(1) + ' ' + bcolors.ENDC
        elif num == 2:
            return bcolors.YELLOW_HIGHLIGHT + str(2) + ' ' + bcolors.ENDC
        elif num == 3:
            return bcolors.MAGENTA_HIGHLIGHT + str(3) + ' ' + bcolors.ENDC
        elif num == 4:
            return bcolors.RED_HIGHLIGHT + str(4) + ' ' + bcolors.ENDC
        elif num == 5:
            return bcolors.BLUE_HIGHLIGHT + str(5) + ' ' + bcolors.ENDC
        elif num == 6:
            return bcolors.GREEN_HIGHLIGHT + str(6) + ' ' + bcolors.ENDC
        else:
            return ''


    def printCube(self):
        string = ''
        for i in range(len(self.top)):
            for _ in range(len(self.top)):
                    string += '  '

            for j in range(len(self.top[i])):
                string += self.stringColor(self.top[i][j])

            for _ in range(len(self.top)):
                string += '  '
            for _ in range(len(self.top[i])):
                string += '  '

            string += '\n'

        for i in range(len(self.front)):
            for j in range(len(self.left[i])):
                string += self.stringColor(self.left[i][j])

            for j in range(len(self.front[i])):
                string += self.stringColor(self.front[i][j])

            for j in range(len(self.right[i])):
                string += self.stringColor(self.right[i][j])

            for j in range(len(self.back[i])):
                string += self.stringColor(self.back[i][j])
            
            string += '\n'

        for i in range(len(self.bottom)):
            for _ in range(len(self.bottom)):
                    string += '  '

            for j in range(len(self.bottom[i])):
                string += self.stringColor(self.bottom[i][j])

            for _ in range(len(self.bottom)):
                string += '  '
            for _ in range(len(self.bottom[i])):
                string += '  '

            string += '\n'

        print(string)