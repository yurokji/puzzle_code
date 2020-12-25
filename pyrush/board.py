from vechle import *
problem_set_file_path ="./problems/problem_set.txt"


class Board:
    def __init__(self, rows=6, cols=6):
        self.rows= rows
        self.cols = cols
        self.grid = []
        self.makeGrid(self.rows + 1)
        self.level = 0
        self.vechles = {}
        self.stages = []
    
        with open(problem_set_file_path, "r") as stageFile:
            for line in stageFile:
                words = line.split(" ")
                stage = []
                for word in words:
                    word = word.strip()
                    block = []
                    for letter in word:
                        if letter.isdigit():
                            block.append(int(letter))
                        else:
                            block.append(letter)
                    stage.append(block)
                self.stages.append(stage)
    
    def __str__(self):
        ret_str = "\n"
        for i in range(self.rows):
            for j in range(self.cols):
                ret_str += str(self.grid[j][i])
                ret_str += " "
            ret_str += "\n"
        ret_str += "\n"
        return ret_str

    def makeGrid(self, size):
        for i in range(size):
            self.grid.append([0]*size)


    def stagePrepare(self):
        self.clearGrid()
        self.vechles = {}
        curr_lev_stage = self.stages[self.level]
        for v in curr_lev_stage:
            self.pushVechle(Vechle(v[0], [v[1], v[2]], v[3]))
            
    def pushVechle(self, vechle):
        vPos = vechle.pos
        vLen = vechle.len
        vDir = vechle.dir
        vKind = vechle.kind

        isUpdated = True

        if vKind in self.vechles:
            return False
        
        if vDir == 'h':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 - vLen and \
                vPos[1] < 0 and vPos[1] > self.rows - 1:
                return False

            for i in range(vPos[0], vPos[0] + vLen):
                if self.grid[i][vPos[1]] != 0:
                    isUpdated = False
                    return False

            if isUpdated:
                self.vechles[vKind] = vechle
                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = vKind
                return True

        elif vDir == 'v':
            if vPos[0] < 0 and vPos[0] > self.cols - 1 and \
                vPos[1] < 0 and vPos[1] > self.rows - 1 - vLen :
                return False

            for i in range(vPos[1], vPos[1] + vLen):
                if self.grid[vPos[0]][i] != 0:
                    isUpdated = False
                    return False

            if isUpdated:
                self.vechles[vKind] = vechle
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][i] = vKind
                return True

    def clearGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 0

    def isOnboard(self, kind):
        if kind not in self.vechles:
            return False
        else:
            return True

    

    def move(self, kind, val):

        if kind not in self.vechles:
            return False

        vechle = self.vechles[kind]
        vPos = vechle.pos
        vLen = vechle.len
        vDir = vechle.dir
        vKind = vechle.kind

        isUpdated = True

        if kind == 'x' and vPos[0] ==  4:
            self.vechles['x'].pos = (6,2)
            return True


        if vDir == 'h':
            if vPos[0] + val < 0 or vPos[0] + val > self.cols - vLen or \
                vPos[1]  < 0 or vPos[1] > self.rows - 1:
                return False

            for i in range(vPos[0] + val, vPos[0]+val + vLen):
                if self.grid[i][vPos[1]] != 0:
                    if self.grid[i][vPos[1]] != vKind:
                        isUpdated = False
                        return False

            if isUpdated:
                if val > 0:
                    self.grid[vPos[0]][vPos[1]] = 0
                else:
                    self.grid[vPos[0] + vLen - 1][vPos[1]]=0
                self.vechles[vKind].pos[0] += val
                vPos = vechle.pos

                for i in range(vPos[0], vPos[0] + vLen):
                    self.grid[i][vPos[1]] = vKind
                return True

        

        elif vDir == 'v':
            if vPos[0] < 0 or vPos[0] > self.cols - 1 or \
                vPos[1] + val < 0 or vPos[1] + val > self.rows - vLen :
                return False

            for i in range(vPos[1] +val, vPos[1]+val + vLen):
                if self.grid[vPos[0]][i] != 0:
                    if self.grid[vPos[0]][i] != vKind:
                        isUpdated = False
                        return False

            if isUpdated:
                if val > 0:
                    self.grid[vPos[0]][vPos[1]] = 0
                else:
                    self.grid[vPos[0]][vPos[1]+vLen - 1]=0
                self.vechles[vKind].pos[1] += val
                vPos = vechle.pos
                self.grid[vPos[0]][vPos[1] - val] = 0
                for i in range(vPos[1], vPos[1] + vLen):
                    self.grid[vPos[0]][i] = vKind
                return True
    def isLevelCleared(self):
        vechle_x = self.vechles['x']
        if vechle_x.pos[0] >= 4 and vechle_x.pos[1] == 2:
            self.vechles['x'].pos = (6,2)
            return True
        else:
            return False






