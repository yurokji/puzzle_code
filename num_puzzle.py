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
    piece_1 = pygame.image.load("./img/1.png")
    piece_1 = pygame.transform.scale(piece_1, (100, 100))
    piece_2 = pygame.image.load("./img/2.png")
    piece_2 = pygame.transform.scale(piece_2, (100, 100))  
    piece_3 = pygame.image.load("./img/3.png")
    piece_3 = pygame.transform.scale(piece_3, (100, 100))
    piece_4 = pygame.image.load("./img/4.png")
    piece_4 = pygame.transform.scale(piece_4, (100, 100)) 
    piece_5 = pygame.image.load("./img/5.png")
    piece_5 = pygame.transform.scale(piece_5, (100, 100))
    piece_6 = pygame.image.load("./img/6.png")
    piece_6 = pygame.transform.scale(piece_6, (100, 100)) 
    piece_7 = pygame.image.load("./img/7.png")
    piece_7 = pygame.transform.scale(piece_7, (100, 100))
    piece_8 = pygame.image.load("./img/8.png")
    piece_8 = pygame.transform.scale(piece_8, (100, 100))
    piece_0 = pygame.image.load("./img/0.png")
    piece_0 = pygame.transform.scale(piece_0, (100, 100))  

    pieces = [[piece_1, piece_2, piece_3], 
              [piece_4, piece_5, piece_6],
              [piece_7, piece_8, piece_0]]


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