MAX_COLS = 6
MAX_ROWS = 6

import pygame
from pygame.locals import *

class Vechle:
    def __init__(self, kind, pos, dir):
        if type(kind) is str:
            self.kind = kind
            if self.kind == "x":
                self.img_name = "./img/x.png"
                self.len = 2
            elif self.kind == "a":
                self.img_name = "./img/a.png"
                self.len = 2
            elif self.kind == "b":
                self.img_name = "./img/b.png"
                self.len = 2
            elif self.kind == "c":
                self.img_name = "./img/c.png"
                self.len = 2
            elif self.kind == "d":
                self.img_name = "./img/d.png"
                self.len = 2
            elif self.kind == "e":
                self.img_name = "./img/e.png"
                self.len = 2
            elif self.kind == "f":
                self.img_name = "./img/f.png"
                self.len = 2
            elif self.kind == "g":
                self.img_name = "./img/g.png"
                self.len = 2
            elif self.kind == "h":
                self.img_name = "./img/h.png"
                self.len = 2
            elif self.kind == "i":
                self.img_name = "./img/i.png"
                self.len = 2
            elif self.kind == "j":
                self.img_name = "./img/j.png"
                self.len = 2
            elif self.kind == "k":
                self.img_name = "./img/k.png"
                self.len = 2
            elif self.kind == "o":
                self.img_name = "./img/o.png"
                self.len = 3
            elif self.kind == "p":
                self.img_name = "./img/p.png"
                self.len = 3
            elif self.kind == "q":
                self.img_name = "./img/q.png"
                self.len = 3
            elif self.kind == "r":
                self.img_name = "./img/r.png"
                self.len = 3
            else:
                raise Exception(kind , "does not belong to any kind")
        else:
            raise Exception(kind, "is not even a string")

        if dir == "h" or  dir == "v":
            self.dir = dir
        else:
            raise Exception("direction should be either 0 or 1")


        if type(pos) is list:
            if pos[0] >= 0 and  pos[0] <= MAX_COLS - 1 and \
                pos[1] >= 0 and pos[1] <= MAX_ROWS - 1:
                self.pos = [pos[0], pos[1]]
            else:
                raise Exception(pos, "is not in the valid number")


        self.image = pygame.image.load(self.img_name)
        self.image = pygame.transform.scale(self.image, (self.len * 100, 100))
        if self.dir == 'v':
            self.image = pygame.transform.rotate(self.image, 90)

        






