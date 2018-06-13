#for tile

import itertools
import pygame
from settings import *
vec = pygame.math.Vector2

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y



class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.image.load('Player\Down1.png').convert_alpha()
        # Player Animation
        self.right1 = pygame.image.load("Player/Right1.png")
        self.right2 = pygame.image.load("Player/Right2.png")
        self.left1 = pygame.image.load("Player/Left1.png")
        self.left2 = pygame.image.load("Player/Left2.png")
        self.up1 = pygame.image.load("Player/Up1.png")
        self.up2 = pygame.image.load("Player/Up2.png")
        self.down1 = pygame.image.load("Player/Down1.png")
        self.down2 = pygame.image.load("Player/Down2.png")
        self.left_attack1 = pygame.image.load("Player/Left_Attack1.png")
        self.left_attack2 = pygame.image.load("Player/Left_Attack2.png")
        self.left_attack3 = pygame.image.load("Player/Left_Attack3.png")
        self.left_attack4 = pygame.image.load("Player/Left_Attack4.png")
        self.right_attack1 = pygame.image.load("Player/Right_Attack1.png")
        self.right_attack2 = pygame.image.load("Player/Right_Attack2.png")
        self.right_attack3 = pygame.image.load("Player/Right_Attack3.png")
        self.right_attack4 = pygame.image.load("Player/Right_Attack4.png")

        self.up_attack1 = pygame.image.load("Player/Up_Attack1.png")
        self.up_attack2 = pygame.image.load("Player/Up_Attack2.png")
        self.up_attack3 = pygame.image.load("Player/Up_Attack3.png")
        self.up_attack4 = pygame.image.load("Player/Up_Attack4.png")

        self.down_attack1 = pygame.image.load("Player/Down_Attack1.png")
        self.down_attack2 = pygame.image.load("Player/Down_Attack2.png")
        self.down_attack3 = pygame.image.load("Player/Down_Attack3.png")
        self.down_attack4 = pygame.image.load("Player/Down_Attack4.png")

        self.right_walk = [self.right1,self.right2]
        self.left_walk = [self.left1, self.left2]
        self.up_walk = [self.up1, self.up2]
        self.down_walk = [self.down1,self.down2]
        self.left_attack = [self.left_attack1, self.left_attack2, self.left_attack3, self.left_attack4]
        self.right_attack = [self.right_attack1, self.right_attack2, self.right_attack3, self.right_attack4]
        self.up_attack = [self.up_attack1, self.up_attack2, self.up_attack3, self.up_attack4]
        self.down_attack = [self.down_attack1, self.down_attack2, self.down_attack3, self.down_attack4]
        

        self.current_frame = 0
        self.walk_anim_frame = 0
        self.attack_anim_frame = 0
        self.last_update = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0,0)
        self.pos = vec(x, y)
        self.direction = 0 # 1: N, 2: W, 3: W, 4:E

    def get_keys(self):
        self.vel = vec(0,0)
        keys = pygame.key.get_pressed()
        # Left
        if keys[pygame.K_a]:
            self.direction = 3
            # loop chara animation
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.left_walk)
                self.image = self.left_walk[self.current_frame]
         
            self.vel.x = -Walk_Speed
            self.image = self.left_walk[self.current_frame]
            
        
        # Right
        elif keys[pygame.K_d]:
            self.direction = 4
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.left_walk)
                self.image = self.right_walk[self.current_frame]
            self.image = self.right_walk[self.current_frame]
            self.vel.x = Walk_Speed

        # Up
        elif keys[pygame.K_w]:
            self.direction = 1
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.left_walk)
                self.image = self.up_walk[self.current_frame]
            self.image = self.up_walk[self.current_frame]
            self.vel.y = -Walk_Speed

        # Down
        elif keys[pygame.K_s]:
            self.direction = 2
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.left_walk)
                self.image = self.down_walk[self.current_frame]
            self.image = self.down_walk[self.current_frame]
            self.vel.y = Walk_Speed

        #Attack left
        if keys[pygame.K_j] and self.direction == 3:
           now = pygame.time.get_ticks()
           if now -self.last_update > 200:
                self.last_update = now
                self.attack_anim_frame = (self.attack_anim_frame + 1) % len(self.left_attack)
                self.image = self.left_attack[self.attack_anim_frame]


        #Attack right
        if keys[pygame.K_j] and self.direction == 4:
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.attack_anim_frame = (self.attack_anim_frame + 1) % len(self.left_attack)
                self.image = self.right_attack[self.attack_anim_frame]

        #Attck Up
        if keys[pygame.K_j] and self.direction == 1:
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.attack_anim_frame = (self.attack_anim_frame + 1) % len(self.left_attack)
                self.image = self.up_attack[self.attack_anim_frame]

        #Attck Down
        if keys[pygame.K_j] and self.direction == 2:
            now = pygame.time.get_ticks()
            if now -self.last_update > 200:
                self.last_update = now
                self.attack_anim_frame = (self.attack_anim_frame + 1) % len(self.left_attack)
                self.image = self.down_attack[self.attack_anim_frame]
  

    def collide_with_walls(self, dir):
        # collision check for x
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x=0
                self.rect.x = self.pos.x
        # collision check for y
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y=0
                self.rect.y = self.pos.y


    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((Tile_size, Tile_size))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * Tile_size
        self.rect.y = y * Tile_size

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y


class intro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.intro_img = pygame.image.load(INTRO_img).convert()

class Mob(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.right1 = pygame.image.load("Player/Right1.png")
        self.right2 = pygame.image.load("Player/Right2.png")
        self.left1 = pygame.image.load("Player/Left1.png")
        self.left2 = pygame.image.load("Player/Left2.png")
        self.up1 = pygame.image.load("Player/Up1.png")
        self.up2 = pygame.image.load("Player/Up2.png")
        self.down1 = pygame.image.load("Player/Down1.png")
        self.down2 = pygame.image.load("Player/Down2.png")
        self.left_walk = [self.left1,self.left2]
        self.right_walk = [self.right1, self.right2]
        self.up_walk = [self.up1, self.up2]
        self.down_walk = [self.down1, self.down2]
        self.image = pygame.image.load("Player/Down1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        
