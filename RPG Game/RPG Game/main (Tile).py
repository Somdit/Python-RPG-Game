import pygame
import random
import sys
from os import path
from settings import*
from sprites import*
from sprites_Tile import*
from tilemap import*


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
        pygame.key.set_repeat(500, 100) #ms,tm
        self.load_data()
        self.Intro = True
        
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'map')
        music_folder = path.join(game_folder, 'Music')
        self.map = TiledMap(path.join(map_folder, Maps))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pygame.image.load('Player\Down1.png').convert_alpha()
        self.mob_img = pygame.image.load('Player\Down1.png').convert_alpha()
        self.intro_img = pygame.image.load('img\player.png').convert()
        # Sound loading
        pygame.mixer.music.load(path.join(music_folder, BG_music))



    def new(self):
        # Reset Game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        # Create the wall * old
        #for row, tiles in enumerate(self.map.data):
        #    for col, tile in enumerate(tiles):
        #        if tile == '1':
        #            Wall(self, col, row)

        
        for tile_object in self.map.tmxdata.objects:
            # The location where player start
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x, tile_object.y)



            if tile_object.name == 'Block':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)



        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.all_sprites.add(self.player)
        self.run() # When the new game start, run it


    def run(self):
        # Game Loop
        self.playing = True
        pygame.mixer.music.play(loops = -1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Gmae Loop Update
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
        # Game Loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug

                   

    
    def draw_grid(self):
        for x in range(0, screen_width, Tile_size):
            pygame.draw.line(self.screen, Light_Grey, (x,0), (x,screen_height))
        for y in range(0, screen_height, Tile_size):
            pygame.draw.line(self.screen, Light_Grey, (0,y), (screen_width, y))

    def draw(self):
        # Game Loop draw
        self.draw_grid()
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, Black, self.camera.apply_rect(sprite.hit_rect),1)
        if self.draw_debug:
            for Block in self.walls:
                pygame.draw.rect(self.screen, Black, self.camera.apply_rect(Block.rect),1)
        
        # after drawing everything, flip the display
        pygame.display.flip()
    

    def show_start_screen(self):
        # Start screen
        if self.Intro:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                Intro = False

            
        
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.show_start_screen()
    g.new()
    g.show_go_screen()

pygame.quit()
