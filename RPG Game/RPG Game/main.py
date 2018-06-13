import pygame
import random
from settings import*
from sprites import*

class Game:
    def __init__(self):
        # Initialize game window
        pygame.init()
        pygame.mixer.init()

        #Create window
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock() #Handle speed
        self.running = True

    def new(self):
        # Reset Game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run() # When the new game start, run it

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Gmae Loop Update
        self.all_sprites.update()

    def events(self):
        # Game Loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
    
    def draw_grid(self):
        for x in range(0, screen_width, Tile_size):
            pygame.draw.line(self.screen, Light_Grey, (x,0), (x,screen_height))
        for y in range(0, screen_height, Tile_size):
            pygame.draw.line(self.screen, Light_Grey, (0,y), (screen_width, y))

    def draw(self):
        # Game Loop draw
        self.screen.fill(White)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pygame.display.flip()
    

    def show_start_screen(self):
        # Start screen
        pass
    
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()