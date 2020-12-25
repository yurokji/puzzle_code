from board import *
import time

pygame.init()
board = Board()
board.stagePrepare()

slide_sound = pygame.mixer.Sound("./sound/slide_sound.wav")
level_sound = pygame.mixer.Sound("./sound/level_sound.wav")
slide_sound.set_volume(0.1)
level_sound.set_volume(0.3)

w = 900
h = 800
stride_x  = 100
stride_y = 100
screen = pygame.display.set_mode((w, h))
bg_img = pygame.image.load("./img/board_img.jpg")
bg_img = pygame.transform.scale(bg_img, (w,h))
pygame.display.set_caption("PyRush Game")
font = pygame.font.SysFont(None, 32)
textLevelImg = font.render('LEVEL: '+ str(board.level+1), True, (255,255,255))
textLevelRect = textLevelImg.get_rect()
textLevelRect.center = (800,250)
textClearImg = font.render('LEVEL CLEARED!', True, (0,255,0), (0,0,255))
textClearRect = textClearImg.get_rect()
textClearRect.center = (w//2,h//2)


running = True
sel_vechle = ""
levClear = False
time_levUp = 0
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not levClear:
                if event.key == K_a:
                    sel_vechle = "a"
                elif event.key == K_b:
                    sel_vechle = "b"
                elif event.key == K_c:
                    sel_vechle = "c"
                elif event.key == K_d:
                    sel_vechle = "d"
                elif event.key == K_e:
                    sel_vechle = "e"
                elif event.key == K_f:
                    sel_vechle = "f"
                elif event.key == K_g:
                    sel_vechle = "g"
                elif event.key == K_h:
                    sel_vechle = "h"
                elif event.key == K_i:
                    sel_vechle = "i"
                elif event.key == K_j:
                    sel_vechle = "j"
                elif event.key == K_k:
                    sel_vechle = "k"
                elif event.key == K_o:
                    sel_vechle = "o"
                elif event.key == K_p:
                    sel_vechle = "p"
                elif event.key == K_q:
                    sel_vechle = "q"
                elif event.key == K_r:
                    sel_vechle = "r"
                elif event.key == K_x:
                    sel_vechle = "x"
                
                elif event.key == pygame.K_LEFT:
                    if board.isOnboard(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'h':
                            print("a is onboard")
                            if board.move(sel_vechle, -1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_RIGHT:
                    if board.isOnboard(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'h':
                            if board.move(sel_vechle, 1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_UP:
                    if board.isOnboard(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'v':
                            if board.move(sel_vechle, -1):
                                pygame.mixer.Sound.play(slide_sound)
                elif event.key == pygame.K_DOWN:
                    if board.isOnboard(sel_vechle):
                        if board.vechles[sel_vechle].dir == 'v':
                            if board.move(sel_vechle, 1):
                                pygame.mixer.Sound.play(slide_sound)

    # print(board)
    screen.blit(bg_img, (0,0))
    for v in board.vechles:
        curr_v = board.vechles[v]
        screen.blit(curr_v.image, (curr_v.pos[0] * stride_x + 100  , curr_v.pos[1] * stride_y + 100))       
    
    textLevelImg = font.render('LEVEL: '+ str(board.level+1), True, (255,255,255))
    screen.blit(textLevelImg, textLevelRect)
    pygame.display.update()


    if levClear == False:
        levClear = board.isLevelCleared()
    
    time_levUp = pygame.time.get_ticks()
    if levClear:
        pygame.mixer.Sound.play(level_sound)
        screen.blit(textClearImg, textClearRect)
        pygame.display.update()
        while pygame.time.get_ticks() - time_levUp < 4000:
            continue

        board.level += 1
        levClear = False
        board.stagePrepare()

    pygame.display.update()
pygame.quit()

            

        




