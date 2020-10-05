import pygame as pg 
import os

FPS = 60
WIDTH, HEIGHT = 750, 750
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 70
BULLET_WIDTH, BULLET_HEIGHT = 50, 50

BLUE_ENEMY = 0
RED_ENEMY = 1
ENEMY_WIDTH, ENEMY_HEIGHT = 60,60
BLUE_ENEMY_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","pixel_ship_blue_small.png")),(ENEMY_WIDTH, ENEMY_HEIGHT))
RED_ENEMY_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","pixel_ship_red_small.png")),(ENEMY_WIDTH, ENEMY_HEIGHT))
ENEMY_BULLET_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","pixel_laser_red.png")),(BULLET_WIDTH, BULLET_HEIGHT))
ENEMY_APPEAR_DURATION = 150
ENEMY_VELOCITY = 2
ENEMY_COOL_DOWN = 100

BULLET_VELOCITY = 8

BG = pg.transform.scale(pg.image.load(os.path.join("assets","background.png")),(WIDTH,HEIGHT))
PLAYER_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","pixel_ship_yellow.png")),(PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_BULLET_IMG = pg.transform.scale(pg.image.load(os.path.join("assets","pixel_laser_green.png")),(BULLET_WIDTH, BULLET_HEIGHT))

PLAYER_HEALTH = 500
PLAYER_VELOCITY = 5