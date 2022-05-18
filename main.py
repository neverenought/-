from pygame import*
from random import randint


screen = display.set_mode((900,600))
display.set_caption('MyGame')

background = transform.scale(image.load('back.png'), (900, 600))

button_play = transform.scale(image.load('play.png'), (200, 80))
button_quit = transform.scale(image.load('exit.png'), (200, 80))


class Game_sprite(sprite.Sprite):
    def __init__(self, image, x,y, w,h  ):
        super(). __init__()
        self.image=  transform.scale(image, (w, h))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self.rect)

class Dino(Game_sprite):
    def __init__(self):
        super().__init__(image.load('dino.png'), 100, 300, 100, 150)
        self.isJump = False
        self.jumpCount = -20

    def update(self):
        if self.isJump:
            self.rect.y += self.jumpCount
            self.jumpCount += 1
            if self.jumpCount > 20:
                self.jumpCount = -20
                self.isJump = False

        super().update()

class Cactus(Game_sprite):
    def __init__(self):
        super().__init__(image.load('cactus.png'),900,350,50,100)

    def update(self):
        self.rect.x -= 6
        if self.rect.x <= -100:
            self.rect.x = 900
        super().update()



screen=display.set_mode((800,500))
background=image.load('C:\\Users\\nchel\\Desktop\\dinogame\\back.png')
background=transform.scale(background, (800,500))

dino = Dino()
cactus = Cactus()
game=True
menu = False
finish = False
clock = time.Clock()

while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x,y = mouse.get_pos()
                if menu:
                    if x >350 and x< 550 and y>200 and y<280:
                        menu = False
                        finish = False
                        
                        dino = Dino()
                        cactus = Cactus()

                    if x > 350 and x <550 and y>400 and y<480:
                        game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                dino.isJump = True


    screen.blit(background,(0,0))
    if menu:
        screen.blit(button_play,(350,200))
        screen.blit(button_quit,(350,400))
    elif not(finish):
        if dino.rect.colliderect(cactus.rect):
            finish = True
            menu = True
        #тут игровой процесс 
        dino.update()
        cactus.update()


    display.update()
