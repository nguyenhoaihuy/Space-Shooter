import pygame as pg 
from s4vsprite import s4vSprite
from const import *

class Bullet(s4vSprite):
    def __init__(self,x,y,img,angle):
        super().__init__(x,y,img)
        self.setAngle(angle)
        self.damage = 50

class Ship(s4vSprite):
    def __init__(self,x,y,img,health=100):
        super().__init__(x,y,img)
        self.health = health
        self.cool_down_counter = 0
        self.bullets = []

    def coolDown(self):
        if self.cool_down_counter != 0:
            self.cool_down_counter -= 1

    def move(self,window):
        self.coolDown()
        self.draw(window)
        for bullet in self.bullets:
            bullet.draw(window)

    def cleanBullets(self):
        self.bullets = list(filter(lambda bullet: bullet.y < HEIGHT and bullet.y + BULLET_HEIGHT > 0,self.bullets))