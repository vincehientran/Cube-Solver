import numpy as np

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

    def isSolved(self):
        solved = True
        solved &= self.top == [[1 for _ in range(3)] for _ in range(3)]
        solved &= self.bottom == [[2 for _ in range(3)] for _ in range(3)]
        solved &= self.front == [[3 for _ in range(3)] for _ in range(3)]
        solved &= self.back == [[4 for _ in range(3)] for _ in range(3)]
        solved &= self.left == [[5 for _ in range(3)] for _ in range(3)]
        solved &= self.right == [[6 for _ in range(3)] for _ in range(3)]
        return solved

    def printCube(self):
        string = ''
        for i in range(len(self.top)):
            for _ in range(len(self.top)):
                    string += ' '

            for j in range(len(self.top[i])):
                string += str(self.top[i][j])

            for _ in range(len(self.top)):
                string += ' '
            for _ in range(len(self.top[i])):
                string += ' '

            string += '\n'

        for i in range(len(self.front)):
            for j in range(len(self.left[i])):
                string += str(self.left[i][j])

            for j in range(len(self.front[i])):
                string += str(self.front[i][j])

            for j in range(len(self.right[i])):
                string += str(self.right[i][j])

            for j in range(len(self.back[i])):
                string += str(self.back[i][j])
            
            string += '\n'

        for i in range(len(self.bottom)):
            for _ in range(len(self.bottom)):
                    string += ' '

            for j in range(len(self.bottom[i])):
                string += str(self.bottom[i][j])

            for _ in range(len(self.bottom)):
                string += ' '
            for _ in range(len(self.bottom[i])):
                string += ' '

            string += '\n'

        print(string)