from ship import Bullet, Ship
from const import *

class Player(Ship):
    def __init__(self,x,y,img,health):
        super().__init__(x,y,img,health)
    
    def shoot(self):
        if self.cool_down_counter == 0:
            new_bullet = Bullet(self.x+PLAYER_WIDTH/2-BULLET_WIDTH/2,self.y,PLAYER_BULLET_IMG,0)
            self.bullets.append(new_bullet)
            self.cool_down_counter = FPS/2

    def move(self,window):
        self.coolDown()
        self.draw(window)
        for bullet in self.bullets:
            bullet.moveForward(10)
            bullet.draw(window)
        self.cleanBullets()