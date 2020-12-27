import pygame
from pygame.locals import QUIT
import time
import random
import sys
num_list = []
m = 5
n = 5
cell_size = 50
w = cell_size * m 
h = cell_size * n
pygame.init()
SURFACE = pygame.display.set_mode((w,h))
FPSCLOCK = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont(None, 30)
text_img = myfont.render("Cleared!", True, (255,0,0)) 
move_type = ['u', 'd', 'l', 'r']

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

num_imgs = []
for y in range(n):
    l = []
    for x in range(m):
        l.append(myfont.render(str(num_list[y][x]), True, (255,0,0))) 
    num_imgs.append(l)

def shuffle_puzzle(num_times):
    for i in range(num_times):
        num = random.randint(0, 3)
        for i in range(n):
            for j in range(m):
                if num_list[i][j] == " ":
                    ii = i
                    jj = j
        # move upward
        if move_type[num] == 'u':

            if ii != n - 1:
                num_list[ii][jj] = num_list[ii + 1][jj]
                num_list[ii + 1][jj] = " "          
        # move downward
        elif move_type[num] == 'd':
            if ii != 0:
                num_list[ii][jj] = num_list[ii - 1][jj]
                num_list[ii - 1][jj] = " "
        # move left
        elif move_type[num] == 'l':
            if jj != m - 1:
                num_list[ii][jj] = num_list[ii][jj+1]
                num_list[ii][jj+1] = " "              
        # move right
        elif move_type[num] == 'r':
            if jj != 0:
                num_list[ii][jj] = num_list[ii][jj-1]
                num_list[ii][jj-1] = " "  

def main():
    # render a text image for game clear
    # init with shuffling the puzzle
    # up, down, left, right for direction
    # ii, jj ; idx for empty cell
    ii = 0 
    jj = 0
   
    shuffle_puzzle(m*n*m)
    for y in range(n):
        for x in range(m):
            print(rect_info[y][x], end=" ")
        print()

    cleared = False
    while True:
        if cleared:
            time.sleep(2)
            cleared = False
            # reshuffle the entire pieces and restart the game
            shuffle_puzzle(m*n*m)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif  event.type == pygame.KEYDOWN:
                blank_found = False
                for i in range(n):
                    for j in range(m):
                        if num_list[i][j] == " ":
                            ii = i
                            jj = j
                            blank_found = True
                            break
                    if blank_found:
                        blank_found = False
                        break
                if event.key == pygame.K_RIGHT:
                    if jj != 0:
                        num_list[ii][jj] = num_list[ii][jj-1]
                        num_list[ii][jj-1] = " "
                elif event.key == pygame.K_LEFT:
                    if jj != m - 1:
                        num_list[ii][jj] = num_list[ii][jj+1]
                        num_list[ii][jj+1] = " "
                elif event.key == pygame.K_UP:
                    if ii != n - 1:
                        num_list[ii][jj] = num_list[ii+1][jj]
                        num_list[ii+1][jj] = " "
                elif event.key == pygame.K_DOWN:
                    if ii != 0:
                        num_list[ii][jj] = num_list[ii-1][jj]
                        num_list[ii-1][jj] = " "

        # check if the game is cleared
        count = 0
        for y in range(n):
            for x in range(m):
                if num_list[y][x] == m * y + x + 1:
                    count += 1
        if count == n * m - 1:
            cleared = True
        SURFACE.fill((0,0,0))
        for i in range(n):
            for j in range(m):
                yPos, xPos  = rect_info[i][j]
                nImg = myfont.render(str(num_list[i][j]), True, (255,0,0))
                SURFACE.blit(nImg, (xPos * cell_size , yPos * cell_size))
        if cleared:
            SURFACE.blit(text_img, (30,130))
        pygame.display.update()

if __name__ == "__main__":
    main()