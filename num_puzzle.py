import pygame
from pygame.locals import QUIT
import time
import random
import sys


# 2d list 3x3
num_list = []
# 1 2 3
# 4 5 6
# 7 8 0 <--0;empty
# 3 * y + x + 1  
# (x= 1, y = 2) ==> 3 * 2 + 1 + 1 = 8
# (x = 2, y = 1) ==> 3 * 1 + 2 + 1 = 6
for x in range(3):
    l = []
    for y in range(3):
        l.append(3 * x + y + 1)
    num_list.append(l)
num_list[2][2] = 0


pygame.init()
SURFACE = pygame.display.set_mode((300,300))
FPSCLOCK = pygame.time.Clock()


def main():

    img = pygame.image.load("./pic.jpg")
    img = pygame.transform.scale(img, (300, 300))
    piece_0 = pygame.image.load("./black.jpeg")
    piece_0 = pygame.transform.scale(piece_0, (100, 100))

    pieces = []
    for i in range(3):
        rowImgs = []
        for j in range(3):
            sImg = img.subsurface((100*j, 100*i, 100, 100))
            rowImgs.append(sImg)
        pieces.append(rowImgs)
    pieces[2][2] = piece_0






    print(num_list)


    # render a text image for game clear
    myfont = pygame.font.SysFont(None, 30)
    text_img = myfont.render("Cleared!", True, (255,0,0)) 


    # init with shuffling the puzzle
    # up, down, left, right for direction

    # ii, jj ; idx for empty cell
    ii = 0 
    jj = 0
    move_type = ['u', 'd', 'l', 'r']
    for _ in range(100):
        num = random.randint(0, 3)
        # move upward
        if move_type[num] == 'u':
            for i in range(3):
                for j in range(3):
                    if num_list[i][j] == 0:
                        ii = i
                        jj = j

            if ii != 2:
                num_list[ii][jj] = num_list[ii + 1][jj]
                num_list[ii + 1][jj] = 0
                pieces[ii][jj] = pieces[ii + 1][jj]
                pieces[ii + 1][jj] = piece_0              
        # move downward
        elif move_type[num] == 'd':
            for i in range(3):
                for j in range(3):
                    if num_list[i][j] == 0:
                        ii = i
                        jj = j

            if ii != 0:
                num_list[ii][jj] = num_list[ii - 1][jj]
                num_list[ii - 1][jj] = 0
                pieces[ii][jj] = pieces[ii - 1][jj]
                pieces[ii - 1][jj] = piece_0   

        # move left
        elif move_type[num] == 'l':
            for i in range(3):
                for j in range(3):
                    if num_list[i][j] == 0:
                        ii = i
                        jj = j

            if jj != 2:
                num_list[ii][jj] = num_list[ii][jj+1]
                num_list[ii][jj+1] = 0
                pieces[ii][jj] = pieces[ii][jj+1]
                pieces[ii][jj+1] = piece_0               
        # move right
        elif move_type[num] == 'r':
            for i in range(3):
                for j in range(3):
                    if num_list[i][j] == 0:
                        ii = i
                        jj = j

            if jj != 0:
                num_list[ii][jj] = num_list[ii][jj-1]
                num_list[ii][jj-1] = 0
                pieces[ii][jj] = pieces[ii][jj-1]
                pieces[ii][jj-1] = piece_0    


    cleared = False
    while True:

        if cleared:
            time.sleep(2)
            cleared = False
            # reshuffle the entire pieces and restart the game
            for _ in range(100):
                num = random.randint(0, 3)
                # move upward
                if move_type[num] == 'u':
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if ii != 2:
                        num_list[ii][jj] = num_list[ii + 1][jj]
                        num_list[ii + 1][jj] = 0
                        pieces[ii][jj] = pieces[ii + 1][jj]
                        pieces[ii + 1][jj] = piece_0              
                # move downward
                elif move_type[num] == 'd':
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if ii != 0:
                        num_list[ii][jj] = num_list[ii - 1][jj]
                        num_list[ii - 1][jj] = 0
                        pieces[ii][jj] = pieces[ii - 1][jj]
                        pieces[ii - 1][jj] = piece_0   

                # move left
                elif move_type[num] == 'l':
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if jj != 2:
                        num_list[ii][jj] = num_list[ii][jj+1]
                        num_list[ii][jj+1] = 0
                        pieces[ii][jj] = pieces[ii][jj+1]
                        pieces[ii][jj+1] = piece_0               
                # move right
                elif move_type[num] == 'r':
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if jj != 0:
                        num_list[ii][jj] = num_list[ii][jj-1]
                        num_list[ii][jj-1] = 0
                        pieces[ii][jj] = pieces[ii][jj-1]
                        pieces[ii][jj-1] = piece_0    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif  event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if jj != 0:
                        num_list[ii][jj] = num_list[ii][jj-1]
                        num_list[ii][jj-1] = 0
                        pieces[ii][jj] = pieces[ii][jj-1]
                        pieces[ii][jj-1] = piece_0  

                elif event.key == pygame.K_LEFT:
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if jj != 2:
                        num_list[ii][jj] = num_list[ii][jj+1]
                        num_list[ii][jj+1] = 0
                        pieces[ii][jj] = pieces[ii][jj+1]
                        pieces[ii][jj+1] = piece_0  
                
                elif event.key == pygame.K_UP:
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if ii != 2:
                        num_list[ii][jj] = num_list[ii+1][jj]
                        num_list[ii+1][jj] = 0
                        pieces[ii][jj] = pieces[ii+1][jj]
                        pieces[ii+1][jj] = piece_0  

                elif event.key == pygame.K_DOWN:
                    for i in range(3):
                        for j in range(3):
                            if num_list[i][j] == 0:
                                ii = i
                                jj = j

                    if ii != 0:
                        num_list[ii][jj] = num_list[ii-1][jj]
                        num_list[ii-1][jj] = 0
                        pieces[ii][jj] = pieces[ii-1][jj]
                        pieces[ii-1][jj] = piece_0  


        # check if the game is cleared
        if num_list[0][0] == 1 and num_list[0][1] == 2 and num_list[0][2] == 3 and \
           num_list[1][0] == 4 and num_list[1][1] == 5 and num_list[1][2] == 6 and \
           num_list[2][0] == 7 and num_list[2][1] == 8:
            cleared = True

        
        print(num_list)
        SURFACE.fill((225,225,225))
        for i in range(3):
            for j in range(3):
                SURFACE.blit(pieces[i][j], (j*100, i*100))


        if cleared:
            SURFACE.blit(text_img, (30,130))

        pygame.display.update()



if __name__ == "__main__":
    main()