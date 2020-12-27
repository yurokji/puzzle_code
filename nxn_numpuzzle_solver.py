import pygame
from pygame.locals import QUIT
import time
import random
import sys
import queue
import copy
import iter

myq = queue.Queue()
num_list = []
m = 3
n = 3
cell_size = 100
w = cell_size * m 
h = cell_size * n
pygame.init()
SURFACE = pygame.display.set_mode((w,h))
FPSCLOCK = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont(None, 70)
text_img = myfont.render("Cleared!", True, (255,0,0)) 


for y in range(n):
    l = []
    for x in range(m):
        l.append(m * y + x + 1)
    num_list.append(l)
num_list[n-1][m-1] = " "

rect_info = []
for y in range(n):
    l = []
    for x in range(m):
        l.append((y, x))
    rect_info.append(l)
print(rect_info)




def shuffle_puzzle(myList, num_times):
    move_type = ['u', 'd', 'l', 'r']
    idx = 0
    while idx < num_times:
        num = random.randint(0, 3)
        for i in range(n):
            for j in range(m):
                if myList[i][j] == " ":
                    blank_i = i
                    blank_j = j
        # move upward
        if move_type[num] == 'u':
            if blank_i != n - 1:
                myList[blank_i][blank_j] = myList[blank_i + 1][blank_j]
                myList[blank_i + 1][blank_j] = " " 
                idx += 1         
        # move downward
        elif move_type[num] == 'd':
            if blank_i != 0:
                myList[blank_i][blank_j] = myList[blank_i - 1][blank_j]
                myList[blank_i - 1][blank_j] = " "
                idx += 1    
        # move left
        elif move_type[num] == 'l':
            if blank_j != m - 1:
                myList[blank_i][blank_j] = myList[blank_i][blank_j+1]
                myList[blank_i][blank_j+1] = " " 
                idx += 1                 
        # move right
        elif move_type[num] == 'r':
            if blank_j != 0:
                myList[blank_i][blank_j] = myList[blank_i][blank_j-1]
                myList[blank_i][blank_j-1] = " "  
                idx += 1    
        print(move_type[num], idx)
        print(myList)

def isSolved(input_list, moves):
    myList = copy.deepcopy(input_list)
    for move in moves:
        for y in range(n):
            for x in range(m):
                if myList[y][x] == " ":
                    blank_i = y
                    blank_j = x
        if move == 'u':
            if blank_i != n - 1:
                myList[blank_i][blank_j] = myList[blank_i + 1][blank_j]
                myList[blank_i + 1][blank_j] = " "          
        # move downward
        elif move == 'd':
            if blank_i != 0:
                myList[blank_i][blank_j] = myList[blank_i - 1][blank_j]
                myList[blank_i - 1][blank_j] = " "
        # move left
        elif move == 'l':
            if blank_j != m - 1:
                myList[blank_i][blank_j] = myList[blank_i][blank_j+1]
                myList[blank_i][blank_j+1] = " "              
        # move right
        elif move == 'r':
            if blank_j != 0:
                myList[blank_i][blank_j] = myList[blank_i][blank_j-1]
                myList[blank_i][blank_j-1] = " "  

    count = 0
    for y in range(n):
        for x in range(m):
            if myList[y][x] == m * y + x + 1:
                count += 1
    if count == n * m - 1:
        print("solution: ", moves)
        print(myList)
        return True
    return False

def valid(input_list, moves):
    myList = copy.deepcopy(input_list)
    for move in moves:
        for y in range(n):
            for x in range(m):
                if myList[y][x] == " ":
                    blank_i = y
                    blank_j = x
        if move == 'u':
            if blank_i != n - 1:
                myList[blank_i][blank_j] = myList[blank_i + 1][blank_j]
                myList[blank_i + 1][blank_j] = " "   
                return True
            else:
                return False
        # move downward
        elif move == 'd':
            if blank_i != 0:
                myList[blank_i][blank_j] = myList[blank_i - 1][blank_j]
                myList[blank_i - 1][blank_j] = " "
                return True
            else:
                return False
        # move left
        elif move == 'l':
            if blank_j != m - 1:
                myList[blank_i][blank_j] = myList[blank_i][blank_j+1]
                myList[blank_i][blank_j+1] = " "   
                return True     
            else:
                return False  
        # move right
        elif move == 'r':
            if blank_j != 0:
                myList[blank_i][blank_j] = myList[blank_i][blank_j-1]
                myList[blank_i][blank_j-1] = " "  
                return True
            else:
                return False
    print("someth")
    return False


def main():
    shuffle_puzzle(num_list, 20)
    copied_num_list = copy.deepcopy(num_list)
    cleared = False
    print("original before: ", num_list)
    solution=""
    myq.put(solution)
    wrong_paths = []
    lenSol = -1
    while not isSolved(copied_num_list, solution): 
        solution = myq.get()  
        if lenSol != len(solution):
            print(str(len(solution)) + " digits")
            lenSol = len(solution)
        for j in ["u", "d", "l", "r"]:
            next_path = solution + j
            if next_path not in wrong_paths: 
                if valid(copied_num_list, next_path):
                    myq.put(next_path)
                    # print(myq.queue)
                else:
                    wrong_paths.append(next_path)
            temp = list(myq.queue)
            temp = list(dict.fromkeys(temp))
            myq.queue = queue.deque(temp)

            


    # show the solution
    print("original after: ", num_list)
    print("copied list after2: ", copied_num_list)
    running = True
    idx = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # time.sleep(2)        
        # move = next(iter(solution))
        if(idx < len(solution)):
            move = solution[idx]
            print(move)
            for y in range(n):
                for x in range(m):
                    if num_list[y][x] == " ":
                        blank_i = y
                        blank_j = x
            if move == 'u':
                if blank_i != n - 1:
                    num_list[blank_i][blank_j] = num_list[blank_i + 1][blank_j]
                    num_list[blank_i + 1][blank_j] = " "
            # move downward
            elif move == 'd':
                if blank_i != 0:
                    num_list[blank_i][blank_j] = num_list[blank_i - 1][blank_j]
                    num_list[blank_i - 1][blank_j] = " "
            # move left
            elif move == 'l':
                if blank_j != m - 1:
                    num_list[blank_i][blank_j] = num_list[blank_i][blank_j+1]
                    num_list[blank_i][blank_j+1] = " "        
            # move right
            elif move == 'r':
                if blank_j != 0:
                    num_list[blank_i][blank_j] = num_list[blank_i][blank_j-1]
                    num_list[blank_i][blank_j-1] = " "  
            idx += 1

        SURFACE.fill((0,0,0))
        for i in range(n):
            for j in range(m):
                yPos, xPos  = rect_info[i][j]
                nImg = myfont.render(str(num_list[i][j]), True, (255,0,0))
                SURFACE.blit(nImg, (xPos * cell_size , yPos * cell_size))
        if cleared:
            SURFACE.blit(text_img, (30,130))
        pygame.display.update()
        FPSCLOCK.tick(0.5)

    pygame.quit()
    

if __name__ == "__main__":
    main()