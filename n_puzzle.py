import pygame
from pygame.locals import QUIT
import time
import random
import sys

m = 3
n = 3
 
w = 0
h = 0
num_shuffles = 0
num_list = []
pieces = []
img = pygame.image.load("./pic.jpg")
piece_0 = pygame.image.load("./black.jpeg")




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

    print(m,n,num_shuffles)

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
    cleared = False
    while True:

        if cleared:
            time.sleep(2)
            shuffle_puzzle(num_list, num_shuffles)
            cleared = False
            # reshuffle the entire pieces and restart the game

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif  event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_RIGHT:
                    if blank_j != 0:
                        num_list[blank_i][blank_j] = num_list[blank_i][blank_j-1]
                        num_list[blank_i][blank_j-1] = m * n
                        pieces[blank_i][blank_j] = pieces[blank_i][blank_j-1]
                        pieces[blank_i][blank_j-1] = piece_0  
                elif event.key == pygame.K_LEFT:
                    if blank_j != m-1:
                        num_list[blank_i][blank_j] = num_list[blank_i][blank_j+1]
                        num_list[blank_i][blank_j+1] = m * n
                        pieces[blank_i][blank_j] = pieces[blank_i][blank_j+1]
                        pieces[blank_i][blank_j+1] = piece_0  
                
                elif event.key == pygame.K_UP:
                    if blank_i != n-1:
                        num_list[blank_i][blank_j] = num_list[blank_i+1][blank_j]
                        num_list[blank_i+1][blank_j] = m * n
                        pieces[blank_i][blank_j] = pieces[blank_i+1][blank_j]
                        pieces[blank_i+1][blank_j] = piece_0  

                elif event.key == pygame.K_DOWN:
                    if blank_i != 0:
                        num_list[blank_i][blank_j] = num_list[blank_i-1][blank_j]
                        num_list[blank_i-1][blank_j] = m * n
                        pieces[blank_i][blank_j] = pieces[blank_i-1][blank_j]
                        pieces[blank_i-1][blank_j] = piece_0  


        # check if the game is cleared
        count = 0
        print(num_list)
        for y in range(n):
            for x in range(m):
                if num_list[y][x] == m * y + x + 1:
                    count += 1
        print("completed tiles: ",count)
        if count == n * m:
            cleared = True

        
        # print(num_list)
        SURFACE.fill((225,225,225))
        for i in range(n):
            for j in range(m):
                SURFACE.blit(pieces[i][j], (j*100, i*100))


        if cleared:
            SURFACE.blit(text_img, (30,130))

        pygame.display.update()



if __name__ == "__main__":
    main(sys.argv[1:])