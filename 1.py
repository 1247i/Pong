
from pygame import *
from random import randint

win_w=1000
win_h=600
img_back='1 (2).jpg'
font.init()
font2=font.Font(None,36)
score=0

lost=0

display.set_caption('Shooter')
window=display.set_mode((win_w,win_h))
background=transform.scale(image.load(img_back),(win_w,win_h))



class GameSprite(sprite.Sprite):
    def __init__(self,iimage,x,y,size_x,size_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(iimage),(65,65))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys [K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_h - 50:
            self.rect.y += self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys [K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_h - 50:
            self.rect.y += self.speed


racket1=Player('racket1.jpg',80,200,500,150,10)
racket2=Player('racket1.jpg',920,200,500,150,10)
ball=GameSprite('ball.png',300,200,50,150,10)
speed_x=5
speed_y=5
finish=False

run = True

while run:
    for e in event.get():
        if e.type ==QUIT:
            run=False
        
    if not finish:
        window.blit(background,(0,0))   
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if racket1.rect.colliderect(ball.rect) or racket2.rect.colliderect(ball.rect):
            speed_x *= -1
        if ball.rect.y > win_h -50 or ball.rect.y <0:
            speed_y *= -1

        
        racket2.reset()
        
        ball.reset() 
        display.update() 
    time.delay(30)      

    