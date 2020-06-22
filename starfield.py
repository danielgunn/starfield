import pygame
from random import uniform, randint
import numpy


(width, height) = (1024, 1024)


class star:
    (x,y,z,sx,sy) = (0.0,0.0,0.0,0,0)

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = uniform(-0.5,0.5)
        self.y = uniform(-0.5,0.5)
        self.z = uniform(0.9,1.0)
        self.c = (randint(0,255), randint(0,255), randint(0,255))

    def update(self, speed):
        self.z -= speed/50

        self.sx = self.x / self.z
        self.sy = self.y / self.z

        if self.sx ==0 or self.sy == 0 or abs(self.sx) > 1 or abs(self.sy) > 1 or self.z < 0.01:
            self.reset()

    def show(self, screen):
        screen_x = int(numpy.interp(self.sx, [-1,1], [0, screen.get_width()]))
        screen_y = int(numpy.interp(self.sy, [-1,1], [0, screen.get_height()]))
        radius = int(numpy.interp(self.z, [0.0001, 1.0], [20, 0]))

        bright = numpy.interp(self.z,[0,1], [1.0,0.0])
        color = tuple(map(lambda x: int(x * bright), self.c))

        pygame.draw.ellipse(screen,color,pygame.Rect(screen_x, screen_y, radius,radius))


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
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for s in stars:
        s.update(1-mouse_y/screen.get_height())
        s.show(screen)

    pygame.display.flip()

