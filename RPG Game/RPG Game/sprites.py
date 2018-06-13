from settings import*
import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite. __init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(Yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.pos = vec(screen_width / 2, screen_height / 2)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

    def update(self):
        self.vel = vec(0, 0)
        # keyboard and movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel.x = -Walk_Speed
            if keys[pygame.K_LSHIFT]:
                self.vel.x = -Run_Speed 
        if keys[pygame.K_d]:
            self.vel.x = Walk_Speed
            if keys[pygame.K_LSHIFT]:
                self.vel.x = Run_Speed 
        if keys[pygame.K_s]:
            self.vel.y = Walk_Speed
            if keys[pygame.K_LSHIFT]:
                self.vel.y = Run_Speed 
        if keys[pygame.K_w]:
            self.vel.y = -Walk_Speed
            if keys[pygame.K_LSHIFT]:
                self.vel.y = -Run_Speed 
        
        # equations of motion
        
        self.pos += self.vel;
        self.rect.center = self.pos
        # set boundaries
        if (self.pos.x > screen_width) or (self.pos.x < 0):
            self.pos.x = 0
        if (self.pos.y > screen_height) or (self.pos.y < 0):
            self.pos.y = 0

