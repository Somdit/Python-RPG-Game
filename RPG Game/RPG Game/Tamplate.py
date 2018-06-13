

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Player Image
        self.image = pygame.image.load('img\player.png').convert()
        self.image.set_colorkey(Black) # Ignore a color so that the character will not have a rectangle shappe
        # Rectangle encloses the sprite 
        self.rect = self.image.get_rect()
        # Put player in the center
        self.rect.center = (screen_width / 2, screen_height / 2) 
        self.y_speed = 5

    def update(self):
        self.rect.x += 5 # repeat right 5
        self.rect.y += self.y_speed
        if self.rect.bottom > screen_height - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > screen_width:
            self.rect.right = 0



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
run = True
while run:
     # Keep loop running at the right speed
    # Input events


    # Update
    

    screen.fill(White)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()
    

   

pygame.quit()
