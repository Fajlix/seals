import pygame
import math

class Pixel:
    def __init__(self, screen, color, pos, size=8):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.size = size
    def update(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.size)

screen = pygame.display.set_mode((800, 650))

pixels = []
x, y = 300, 200
step = 20
angle = 0
for i in range(36):
    x -= math.sin(angle*math.pi/180) * step
    y += math.cos(angle*math.pi/180) * step 
    angle += 10
    pixels.append(Pixel(screen, "orange", (x, y)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(0)
    for p in pixels:
        p.update()
    pygame.display.update()