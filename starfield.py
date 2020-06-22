import pygame
import random
import numpy


(width, height) = (1024, 1024)


class star:
    x,y,z = 0,0,0

    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(-width//2, width//2)
        self.y = random.randint(-height//2, height//2)
        self.z = random.randint(1, width)

    def update(self):
        self.z -= 4

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
    for s in stars:
        s.update()
        s.show(screen)

    pygame.display.flip()

