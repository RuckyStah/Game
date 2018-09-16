import pygame as pg

pg.init()
width = 400
height = 400
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()
        
        self.width = width
        self.height = height
        self.speed = width
        self.color = (0, 0, 0)
        self.x_move = self.speed
        self.y_move = 0


        self.image = pg.Surface((self.width, self.height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        pg.draw.rect(self.image, self.color, [30, 20, self.width, self.height])


    def events(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.x_move = -self.speed
            self.y_move = 0
        if key[pg.K_RIGHT]:
            self.x_move = self.speed
            self.y_move = 0
        if key[pg.K_UP]:
            self.x_move = 0
            self.y_move = -self.speed
        if key[pg.K_DOWN]:
            self.x_move = 0
            self.y_move = self.speed


    def update(self):
        self.events()
        self.wall_check()
        self.rect.x += self.x_move
        self.rect.y += self.y_move

    def wall_check(self):
        desired_x = self.rect.x + self.x_move
        desired_y = self.rect.y + self.y_move
        
        if desired_x < 0 or desired_x + self.width > 400:
            self.x_move = 0
        if desired_y < 0 or desired_y + self.height > 400:
            self.y_move = 0
        
            


        
on = True
player = Player(20, 20, 2)
player_group = pg.sprite.Group()
player_group.add(player)

while on:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            on = False

    player_group.update()


    screen.fill((255, 255, 255))
    player_group.draw(screen)
    pg.display.update()
    clock.tick(1)

pg.quit()
