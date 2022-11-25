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

class Graphics:
    def __init__(self, width, height, pixelSize=8):
        self.width = width+pixelSize/2
        self.height = height+pixelSize/2
        self.pixelSize = pixelSize
        self.pixels = []

        self.screen = pygame.display.set_mode((self.width, self.height))

    def drawHuman(self, listOfPos):
        for pos in listOfPos:
            self.pixels.append(Pixel(self.screen, "orange", pos, self.pixelSize))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(0)
            for p in self.pixels:
                p.update()
            pygame.display.update()

    def simulate(self):
        1
        #TODO this will simulate for eternity