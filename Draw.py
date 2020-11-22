###############################################################################
#   Name of the class: Draw
#   Date of creation: 19/10/2020
#   Description:   In this class we have the algorithm to draw an image of the
#                  maze, powered by the pygame library.
################################################################################

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from pygame.locals import *
from Jsonfile import JsonFile

GREEN = (0, 143, 57)
GREY = (230, 230, 230)
BLACK = (0, 0, 0)
GREEN_2 = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (169, 131, 7)
BLUE = (0, 0, 255)
CYAN = (0, 132, 255)
BG_BLUE = (224, 255, 255)
BROWN = (194, 155, 97)
WHITE = (0, 0, 0)

class Draw:
    """Constructor"""

    def __init__(self, grid, title):
        self.nRows, self.nColumns = grid.size()
        self.CW = 20
        self.CH = 20
        self.XMARGIN = 20
        self.YMARGIN = 120
        self.grid = grid
        self.title = title
        self.WW = self.CW * self.nColumns + self.XMARGIN
        self.WH = self.CH * self.nRows + self.YMARGIN

    def draw(self):
        pygame.init()
        BIT_COLOR_32 = 32
        background = pygame.display.set_mode((self.WW, self.WH), pygame.RESIZABLE, BIT_COLOR_32)
        pygame.display.set_caption(self.title)

        background.fill(BG_BLUE)  # Colour of the background

        save_img = pygame.image.load('images/btnSave.png')  # We load save icon
        save_img = pygame.transform.scale(save_img, (20, 20))  # We scale it
        background.blit(save_img, (8, 8))

        """
        Basically, algorithm draw a line(a wall) if a cell is NOT linked with another. If two cells are linked
        we don´t draw.
        """
        y_axis = self.YMARGIN / 2  # x offset
        for row in self.grid.all_rows():
            x_axis = self.XMARGIN / 2  # y offset
            for cell in row:
                if cell is not None:

                    if not cell.isLinked(cell.cellNorth):
                        pygame.draw.line(background, WHITE, (x_axis, y_axis), (x_axis + self.CW, y_axis), 5)

                    if not cell.isLinked(cell.cellSouth):
                        pygame.draw.line(background, WHITE, (x_axis, y_axis + self.CH),
                                         (x_axis + self.CW, y_axis + self.CH), 5)

                    if not cell.isLinked(cell.cellWest):
                        pygame.draw.line(background, WHITE, (x_axis, y_axis), (x_axis, y_axis + self.CH), 5)

                    if not cell.isLinked(cell.cellEast):
                        pygame.draw.line(background, WHITE, (x_axis + self.CW, y_axis),
                                         (x_axis + self.CW, y_axis + self.CH), 5)

                    if cell.getValue() == 0:
                        pygame.draw.rect(background, GREY, [x_axis, y_axis, self.CW, self.CH], 0)
                    elif cell.getValue() == 1:
                        pygame.draw.rect(background, BROWN, [x_axis, y_axis, self.CW, self.CH], 0)
                    elif cell.getValue() == 2:
                        pygame.draw.rect(background, GREEN_2, [x_axis, y_axis, self.CW, self.CH], 0)
                    elif cell.getValue() == 3:
                        pygame.draw.rect(background, CYAN, [x_axis, y_axis, self.CW, self.CH], 0)
                x_axis = x_axis + self.CW
            y_axis = y_axis + self.CH

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # If we click on the save image we save the json and png
                    x, y = event.pos
                    if save_img.get_rect().collidepoint(x, y):
                        pygame.image.save(background,
                                          'Maze ' + str(self.grid.rows) + 'x' + str(self.grid.columns) + '.png')
                        JsonFile.export(self.grid)
                if event.type == QUIT:  # If we close the window, the program ends.
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
