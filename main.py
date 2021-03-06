import pygame as pg 
import os
import time
import random
from const import *
from ship import Bullet, Ship
from player import Player
from enemy import Enemy

#initialize pygame
pg.init()

#create screen
WIN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Space Shooter Tutorial")



#main function
def main():
    run = True
    clock = pg.time.Clock()
    #set score
    score = 0
    #create player
    player = Player(WIDTH//2-PLAYER_WIDTH/2,HEIGHT-100,PLAYER_IMG,500)
    #enemy
    enemies = []
    enemy_appear_timer = 0
    #font
    main_font = pg.font.SysFont("comicsans", 50)
    # add random an enemy
    def addEnemy():
        nonlocal enemy_appear_timer
        if enemy_appear_timer == 0:
            x_pos = random.randrange(0,WIDTH-ENEMY_WIDTH)
            enemy_type = random.choice([BLUE_ENEMY,RED_ENEMY])
            if enemy_type == BLUE_ENEMY:
                new_enemy = Enemy(x_pos, -30-ENEMY_HEIGHT,BLUE_ENEMY_IMG,BLUE_ENEMY)
                enemies.append(new_enemy)
            if enemy_type == RED_ENEMY:
                new_enemy = Enemy(x_pos, -30-ENEMY_HEIGHT,RED_ENEMY_IMG,RED_ENEMY)
                enemies.append(new_enemy)
            enemy_appear_timer = ENEMY_APPEAR_DURATION
        enemy_appear_timer -= 1
    
    # clean all enemy out of window
    def cleanEnemy(): # NO NEED FOR THIS
        pass
        #nonlocal enemies
        #enemies = list(filter(lambda enemy: enemy.y < HEIGHT,enemies))

    # main function to redraw all objects
    def redraw_window():
        WIN.blit(BG,(0,0))
        player.move(WIN)
        addEnemy()
        #draw score and health
        score_text = main_font.render(f"score: {score}", 1, (255, 255, 255))
        hp_text = main_font.render(f"health: {player.health}", 1, (255, 255, 255))

        WIN.blit(score_text, (10, 10))
        WIN.blit(hp_text, (WIDTH - hp_text.get_width() - 10, 10))

        for enemy in enemies:
            enemy.move(WIN)
        #cleanEnemy()
        pg.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and player.y - PLAYER_VELOCITY > 0:
            player.y -= PLAYER_VELOCITY
        if keys[pg.K_DOWN] and player.y + PLAYER_VELOCITY < HEIGHT-PLAYER_HEIGHT:
            player.y += PLAYER_VELOCITY
        if keys[pg.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
            player.x -= PLAYER_VELOCITY
        if keys[pg.K_RIGHT] and player.x + PLAYER_VELOCITY < WIDTH-PLAYER_WIDTH:
            player.x += PLAYER_VELOCITY
        if keys[pg.K_SPACE]:
            player.shoot()



        for enemy in enemies:
            if enemy.isCollidedWith(player):
                player.health -= 10
                enemies.remove(enemy)
            for bullet in enemy.bullets:
                if bullet.isCollidedWith(player):
                    player.health -= 10
                    enemy.bullets.remove(bullet)
            for bullet in player.bullets:
                if bullet.isCollidedWith(enemy):
                    score += 1
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
            if enemy.y > HEIGHT:
                player.health -= 100
                enemies.remove(enemy)
            if player.health <= 0:
                run = False


main()
