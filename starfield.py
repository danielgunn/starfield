import pygame
import random
import numpy


width = 800
height = 800


class star:
    x,y,z = 0,0,0

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.z = random.randint(50, width)

    def update(self):
        self.z -= 1

        if self.z < 10:
            self.reset()

    def show(self, screen):
        sx = int(numpy.interp(self.x / self.z, [0, 1], [0, width]))
        sy = int(numpy.interp(self.y / self.z, [0, 1], [0, width]))

        r = int(numpy.interp(self.z, [0, width], [10, 0]))

        bright = numpy.interp(self.z,[0,width], [1.0,0.0])
        color = tuple(map(lambda x: int(x * bright), (255,255,10)))

        pygame.draw.ellipse(screen,color,pygame.Rect(sx, sy, r,r))

pygame.init()
screen = pygame.display.set_mode((width, height))

done = False

stars = []
for i in range(100):
    stars.append(star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    for s in stars:
        s.update()
        s.show(screen)

    pygame.display.flip()
    #pygame.transform.scale(screen, (int(width / 2), int(height / 2)))

