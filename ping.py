from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.y += self.speed
class Player2(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()

racket1 = Player1('racket.png', 30, 200, 4, 50, 150)
racket2 = Player2('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200 , 4, 50, 50)
spx = 3
spy = 3
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 500:
        finish = True
        window.blit(lose2, (200, 200))
    if finish != True:
        ball.rect.x += spx
        ball.rect.y += spy
        window.fill(back)
        racket1.reset()
        racket1.update()
        racket2.reset()
        racket2.update()
        ball.reset()
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        spy *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        spx *= -1
    display.update()
    time.delay(20)