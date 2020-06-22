import pygame
import random
import numpy


width = 1024
height = 1024


class star:
    x,y,z = 0,0,0

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.z = random.randint(50, width)

    def update(self):
        self.z -= 2

        if self.z < 10:
            self.reset()

    def show(self, screen):
        sx = int(numpy.interp(self.x / self.z, [-1, 1], [-width, width]))
        sy = int(numpy.interp(self.y / self.z, [-1, 1], [-height, height]))

        r = int(numpy.interp(self.z, [0, width], [20, 0]))

        bright = numpy.interp(self.z,[0,width], [1.0,0.0])
        color = tuple(map(lambda x: int(x * bright), (255,255,55)))

        pygame.draw.ellipse(screen,color,pygame.Rect(int(sx+width/2), int(sy+height/2), r,r))


pygame.init()
screen = pygame.display.set_mode((width, height))

done = False

stars = []
for i in range(200):
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

