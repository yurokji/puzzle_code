import pygame
from pygame.locals import QUIT
import time
import random
import sys
from queue import PriorityQueue
import copy

m = 3
n = 3
 
w = 0
h = 0
num_shuffles = 0
num_list = []
pieces = []
img = pygame.image.load("./pic.jpg")
piece_0 = pygame.image.load("./black.jpeg")

my_q = PriorityQueue()


def isValid(input_list, moves):
    blank_i = 0
    blank_j = 0
    for move in moves:
        found = False
        for i in range(n):
            for j in range(m):
                if input_list[i][j] == m*n:
                    blank_i = i
                    blank_j = j
                    found = True
                    break
            if found:
                found = False
                break

        # move upward
        if move == 'u':
            if blank_i != n - 1:
                input_list[blank_i][blank_j] = input_list[blank_i + 1][blank_j]
                input_list[blank_i + 1][blank_j] = m * n
            else:
                return False          
        # move downward
        elif move == 'd':
            if blank_i != 0:
                input_list[blank_i][blank_j] = input_list[blank_i - 1][blank_j]
                input_list[blank_i - 1][blank_j] = m * n
            else:
                return False 

        # move left
        elif move == 'l':
            if blank_j != m - 1:
                input_list[blank_i][blank_j] = input_list[blank_i][blank_j+1]
                input_list[blank_i][blank_j+1] = m * n
            else:
                return False 
        # move right
        elif move == 'r':
            if blank_j != 0:
                input_list[blank_i][blank_j] = input_list[blank_i][blank_j-1]
                input_list[blank_i][blank_j-1] = m * n
            else:
                return False 
    return True


def isSolved(input_list, moves):
    blank_i = 0
    blank_j = 0
    for move in moves:
        found = False
        for i in range(n):
            for j in range(m):
                if input_list[i][j] == m*n:
                    blank_i = i
                    blank_j = j
                    found = True
                    break
            if found:
                found = False
                break

        # move upward
        if move == 'u':
            if blank_i != n - 1:
                input_list[blank_i][blank_j] = input_list[blank_i + 1][blank_j]
                input_list[blank_i + 1][blank_j] = m * n
         
        # move downward
        elif move == 'd':
            if blank_i != 0:
                input_list[blank_i][blank_j] = input_list[blank_i - 1][blank_j]
                input_list[blank_i - 1][blank_j] = m * n

        # move left
        elif move == 'l':
            if blank_j != m - 1:
                input_list[blank_i][blank_j] = input_list[blank_i][blank_j+1]
                input_list[blank_i][blank_j+1] = m * n

        # move right
        elif move == 'r':
            if blank_j != 0:
                input_list[blank_i][blank_j] = input_list[blank_i][blank_j-1]
                input_list[blank_i][blank_j-1] = m * n

    if numTilesInPlace(input_list) == m * n:
        return True
    return False

def numTilesInPlace(input_list):
    count = 0
    for y in range(n):
        for x in range(m):
            if input_list[y][x] == m * y + x + 1:
                count += 1
    # print("count: ", count)
    return count

def shuffle_puzzle(myList, num_times):
    move_type = ['u', 'd', 'l', 'r']
    blank_i = 0
    blank_j = 0
    idx = 0
    while idx < num_times:
        num = random.randint(0, 3)
        found = False
        for i in range(n):
            for j in range(m):
                if num_list[i][j] == m*n:
                    blank_i = i
                    blank_j = j
                    found = True
                    break
            if found:
                break

        # move upward
        if move_type[num] == 'u':
            if blank_i != n - 1:
                num_list[blank_i][blank_j] = num_list[blank_i + 1][blank_j]
                num_list[blank_i + 1][blank_j] = m * n
                pieces[blank_i][blank_j] = pieces[blank_i + 1][blank_j]
                pieces[blank_i + 1][blank_j] = piece_0   
                idx += 1           
        # move downward
        elif move_type[num] == 'd':
            if blank_i != 0:
                num_list[blank_i][blank_j] = num_list[blank_i - 1][blank_j]
                num_list[blank_i - 1][blank_j] = m * n
                pieces[blank_i][blank_j] = pieces[blank_i - 1][blank_j]
                pieces[blank_i - 1][blank_j] = piece_0  
                idx += 1 

        # move left
        elif move_type[num] == 'l':
            if blank_j != m - 1:
                num_list[blank_i][blank_j] = num_list[blank_i][blank_j+1]
                num_list[blank_i][blank_j+1] = m * n
                pieces[blank_i][blank_j] = pieces[blank_i][blank_j+1]
                pieces[blank_i][blank_j+1] = piece_0  
                idx += 1             
        # move right
        elif move_type[num] == 'r':
            if blank_j != 0:
                num_list[blank_i][blank_j] = num_list[blank_i][blank_j-1]
                num_list[blank_i][blank_j-1] = m * n
                pieces[blank_i][blank_j] = pieces[blank_i][blank_j-1]
                pieces[blank_i][blank_j-1] = piece_0    
                idx += 1



def main(options):
    global m, n, w, h, num_shuffles, num_list, pieces, img, piece_0
    m = int(options[0])
    n = int(options[1])
    
    num_shuffles = int(options[2])
    cell_size = 100
    cell_size2 = int(cell_size * 0.96)
    
    w = cell_size * m
    h = cell_size * n

    pygame.init()
    SURFACE = pygame.display.set_mode((w,h))
    FPSCLOCK = pygame.time.Clock()


    # render a text image for game clear
    myfont = pygame.font.SysFont(None, 50)
    text_img = myfont.render("Cleared!", True, (255,0,0)) 

   

    blank_i = 0
    blank_j = 0

    for x in range(n):
        l = []
        for y in range(m):
            l.append(m * x + y + 1)
        num_list.append(l)
    print(num_list)
    pieces = []

    img = pygame.transform.scale(img, (m*cell_size, n*cell_size))
    piece_0 = pygame.transform.scale(piece_0, (cell_size, cell_size))

    for i in range(n):
        rowImgs = []
        for j in range(m):
            sImg = img.subsurface((100*j, 100*i, cell_size2, cell_size2))
            rowImgs.append(sImg)
        pieces.append(rowImgs)
    pieces[n-1][m-1] = piece_0




    blank_i = 0 
    blank_j = 0
    shuffle_puzzle(num_list, num_shuffles)
    # num_list = [[5, 3, 6], [2, 9, 1], [4, 7, 8]]
    print("list before: ", num_list)


    copied_num_list = copy.deepcopy(num_list)
    # find the solution using BFS
    solution =""
    # curr_cost = length of solution so far
    # future_cost = num. not match tiles 

    curr_cost = len(solution)
    future_cost = m*n - 1 - numTilesInPlace(copied_num_list)
    cost = curr_cost + future_cost
    my_q.put((cost, solution))
    num_try = 0
    while not isSolved(copied_num_list, solution):
        solution = my_q.get()[1]
        
        for j in ["u", "d", "l", "r"]:
            num_try += 1
            if num_try % 10000 == 0:
                print("trying out "+str(num_try)+"th solution")
            next_path = solution + j
            copied_num_list = copy.deepcopy(num_list)
            if isValid(copied_num_list, next_path):
                curr_cost = len(solution)
                future_cost = m*n - 1 - numTilesInPlace(copied_num_list)
                cost = curr_cost + future_cost
                my_q.put((cost, next_path))
        copied_num_list = copy.deepcopy(num_list)

    # after finding out the solution 
    print("solution: ", solution)
    print("list after: ", copied_num_list)



    # display the solution


    
    cleared = False
    idx = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if idx < len(solution):
            move = solution[idx]
            found = False
            for i in range(n):
                for j in range(m):
                    if num_list[i][j] == m * n:
                        blank_i = i
                        blank_j = j
                        found = True
                        break
                if found:
                    break
            print(move)
            if move == 'r':
                if blank_j != 0:
                    num_list[blank_i][blank_j] = num_list[blank_i][blank_j-1]
                    num_list[blank_i][blank_j-1] = m * n
                    pieces[blank_i][blank_j] = pieces[blank_i][blank_j-1]
                    pieces[blank_i][blank_j-1] = piece_0  
            elif move == 'l':
                if blank_j != m-1:
                    num_list[blank_i][blank_j] = num_list[blank_i][blank_j+1]
                    num_list[blank_i][blank_j+1] = m * n
                    pieces[blank_i][blank_j] = pieces[blank_i][blank_j+1]
                    pieces[blank_i][blank_j+1] = piece_0  
            
            elif move == 'u':
                if blank_i != n-1:
                    num_list[blank_i][blank_j] = num_list[blank_i+1][blank_j]
                    num_list[blank_i+1][blank_j] = m * n
                    pieces[blank_i][blank_j] = pieces[blank_i+1][blank_j]
                    pieces[blank_i+1][blank_j] = piece_0  

            elif move == 'd':
                if blank_i != 0:
                    num_list[blank_i][blank_j] = num_list[blank_i-1][blank_j]
                    num_list[blank_i-1][blank_j] = m * n
                    pieces[blank_i][blank_j] = pieces[blank_i-1][blank_j]
                    pieces[blank_i-1][blank_j] = piece_0  
            idx += 1

     
        # print(num_list)
        SURFACE.fill((225,225,225))
        for i in range(n):
            for j in range(m):
                SURFACE.blit(pieces[i][j], (j*100, i*100))


        if cleared:
            SURFACE.blit(text_img, (30,130))

        pygame.display.update()
        FPSCLOCK.tick(1)



if __name__ == "__main__":
    main(sys.argv[1:])