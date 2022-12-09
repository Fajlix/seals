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

    def drawSimulation(self, positions, health_points, stage, split):
        self.pixels = []
        for pos, hp in zip(positions, health_points):
            scaled_hp = max(0,int(hp*2.55))
            color = pygame.Color(255 - scaled_hp,scaled_hp,0,0)
            self.pixels.append(Pixel(self.screen, color, pos, self.pixelSize))
        self.screen.fill(0)
        if stage and split:
            self.pixels.append(Pixel(self.screen, "green", (500, 10), self.pixelSize/4))
            pygame.draw.rect(self.screen, color, pygame.Rect(20, 10, 480, 920),  2)
            pygame.draw.rect(self.screen, color, pygame.Rect(500, 10, 480, 920),  2)
        elif stage:
            self.pixels.append(Pixel(self.screen, "green", (500, 10), self.pixelSize/4))
            pygame.draw.rect(self.screen, color, pygame.Rect(20, 10, 960, 920),  2)
        else:
            self.pixels.append(Pixel(self.screen, "green", (500, 500), self.pixelSize/4))
        for p in self.pixels:
            p.update()
        pygame.display.flip()



    def drawHuman(self, listOfInfo, color="orange"):
        self.pixels = []
        for info in listOfInfo:
            pos = info[0]
            scaled_health = int(info[1] * 2.55)
            color = pygame.Color(255 - scaled_health,scaled_health,0,0)
            self.pixels.append(Pixel(self.screen, color, pos, self.pixelSize))
        # green dot in the middle
        self.pixels.append(Pixel(self.screen, "green", (500, 500), self.pixelSize/4))
        self.screen.fill(0)
        for p in self.pixels:
            p.update()
        pygame.display.update()
    
    def drawHuman_stage(self, listOfPos, color="orange"):
        self.pixels = []
        for pos in listOfPos:
            self.pixels.append(Pixel(self.screen, color, pos, self.pixelSize))
        # green dot in the middle
        self.pixels.append(Pixel(self.screen, "green", (500, 10), self.pixelSize/4))
        self.screen.fill(0)
        #draw stage
        pygame.draw.rect(self.screen, color, pygame.Rect(20, 10, 960, 920),  2)
        
        for p in self.pixels:
            p.update()
        pygame.display.flip()

    def drawHuman_stage_split(self, listOfPos, color="orange"):
        self.pixels = []
        for pos in listOfPos:
            self.pixels.append(Pixel(self.screen, color, pos, self.pixelSize))
        # green dot in the middle
        self.pixels.append(Pixel(self.screen, "green", (500, 10), self.pixelSize/4))
        self.screen.fill(0)
        #draw stage
        pygame.draw.rect(self.screen, color, pygame.Rect(20, 10, 480, 920),  2)
        pygame.draw.rect(self.screen, color, pygame.Rect(500, 10, 480, 920),  2) 
        
        for p in self.pixels:
            p.update()
        pygame.display.flip()

    def getPixels(self):
        return self.pixels

    def simulate(self):
        1
        #TODO this will simulate for eternity