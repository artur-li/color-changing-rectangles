import pygame, sys, random

# set up screen
screen = pygame.display.set_mode((560,600))
clock = pygame.time.Clock()

# list of x coordinates for rects
x_positions_list = [i*40 for i in range(1,14,2)]

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,600))
        self.image.fill(self.random_color())
        self.rect = self.image.get_rect()

    def random_color(self):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        return (red,green,blue)
    
    def placement(self):
        global x_positions_list
        if len(x_positions_list) > 0:
            x_position = x_positions_list.pop(0)
            self.rect.centery = 300
            self.rect.centerx = x_position

    def change_color(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.image.fill(self.random_color())

    def update(self):
        self.placement()
        self.change_color()

# create sprite group
rect_group = pygame.sprite.Group()

# spawn 14 rectangles
for i in range(14):
    rect = Rect()
    rect_group.add(rect)

while True:

    for event in pygame.event.get():
        # close if x pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw the rects
    rect_group.update()
    rect_group.draw(screen)
    # update screen 60 fps
    pygame.display.update()
    clock.tick(60)
