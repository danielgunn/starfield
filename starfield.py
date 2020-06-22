import pygame
from random import uniform
import numpy


(width, height) = (1024, 1024)


class star:
    (x,y,z) = (0.0,0.0,0.0)

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = uniform(-0.5,0.5)
        self.y = uniform(-0.5,0.5)
        self.z = uniform(0.2,1.0)

    def update(self):
        self.z -= 0.0025

        sx = self.x / self.z
        sy = self.y / self.z

        if sx ==0 or sy == 0 or abs(sx) > 1 or abs(sy) > 1 or self.z < 0.01:
            self.reset()

    def show(self, screen):
        screen_x = numpy.interp(self.x / self.z, [-1,1], [0, screen.get_width()])
        screen_y = numpy.interp(self.y / self.z, [-1,1], [0, screen.get_height()])
        radius = int(numpy.interp(self.z, [0.0001, 1.0], [20, 0]))

        bright = numpy.interp(self.z,[0,1], [1.0,0.0])
        color = tuple(map(lambda x: int(x * bright), (255,255,55)))

        pygame.draw.ellipse(screen,color,pygame.Rect(int(screen_x), int(screen_y), radius,radius))


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Field")

done = False

stars = []
for i in range(200):
    stars.append(star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    stars.sort(key=lambda x: -x.z)

    for s in stars:
        s.update()
        s.show(screen)

    pygame.display.flip()

