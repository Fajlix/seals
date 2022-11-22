import pygame
import math
import random

class Pixel:
    def __init__(self, screen, color, pos, size=8):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.size = size
    def update(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)
    def getSize(self):
        return self.size

class Graphics:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        self.screen = pygame.display.set_mode((self.width, self.height))

    def drawHuman(self):
        for i in range(10):
            x = Pixel.getSize()/2 + random.random()*(self.width-Pixel.getSize()/2)
            y = Pixel.getSize()/2 + random.random()*(self.height-Pixel.getSize()/2)
            self.pixels.append(Pixel(self.screen, "orange", (x, y)))

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
        while True:
            1