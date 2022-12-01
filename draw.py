import pygame
from agents import Agent

class Pixel:
    def __init__(self, screen, color, pos, size):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.size = size
    def update(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)
    def getSize(self):
        return self.size
    def getPosition(self):
        return self.pos

class Graphics:
    def __init__(self, width, height, pixelSize=8):
        self.width = width+pixelSize/2
        self.height = height+pixelSize/2
        self.pixelSize = pixelSize
        self.pixels = []

        self.screen = pygame.display.set_mode((self.width, self.height))

    def drawHuman(self, listOfPos, color="orange"):
        self.pixels = []
        for pos in listOfPos:
            self.pixels.append(Pixel(self.screen, color, pos, self.pixelSize))
        # green dot in the middle
        self.pixels.append(Pixel(self.screen, "green", (500, 500), self.pixelSize/4))
        self.screen.fill(0)
        for p in self.pixels:
            p.update()
        pygame.display.update()

    def getPixels(self):
        return self.pixels

    def simulate(self):
        1
        #TODO this will simulate for eternity