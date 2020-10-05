from ship import Bullet, Ship
from const import *

class Enemy(Ship):
    def __init__(self,x,y,img,enemy_type,health=100):
        super().__init__(x,y,img,health)
        self.type = enemy_type
        self.setAngle(180)

    def move(self,window):
        self.shoot()
        self.coolDown()
        self.moveForward(ENEMY_VELOCITY)
        self.draw(window)
        for bullet in self.bullets:
            bullet.moveForward(BULLET_VELOCITY)
            bullet.draw(window)
            
        self.cleanBullets()

    def shoot(self):
        if self.cool_down_counter == 0:
            if self.type == BLUE_ENEMY:
                new_bullet = Bullet(self.x+PLAYER_WIDTH/2-BULLET_WIDTH/2,self.y,ENEMY_BULLET_IMG,180)
                self.bullets.append(new_bullet)

            if self.type == RED_ENEMY:
                new_bullet1 = Bullet(self.x+PLAYER_WIDTH/2-BULLET_WIDTH/2,self.y,ENEMY_BULLET_IMG,180)
                self.bullets.append(new_bullet1)
                new_bullet2 = Bullet(self.x+PLAYER_WIDTH/2-BULLET_WIDTH/2,self.y,ENEMY_BULLET_IMG,135)
                self.bullets.append(new_bullet2)
                new_bullet3 = Bullet(self.x+PLAYER_WIDTH/2-BULLET_WIDTH/2,self.y,ENEMY_BULLET_IMG,225)
                self.bullets.append(new_bullet3)

            self.cool_down_counter = ENEMY_COOL_DOWN