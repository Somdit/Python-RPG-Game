import pygame
vec = pygame.math.Vector2

#settings
Title = "Ultimate Spirit"

#screen size
screen_width = 600
screen_height = 450
FPS = 60

#Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Dark_Grey = (40, 40, 40)
Light_Grey = (100, 100, 100)

BG_Color = Dark_Grey

#Player Properties
Walk_Speed = 100
Run_Speed = 200
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)

Tile_size = 16
Grid_width = screen_width / Tile_size
Grid_height = screen_height / Tile_size

Player_img = 'Down1.png'
Player_up1 = 'link_up1.png'
Player_up2 = 'link_up2.png'
Player_left1 = 'link_left1.png'
Player_left2 = 'link_left2.png'
Player_right1 = 'walk_right1.png'
Player_right2 = 'link_right2.png'
Player_down1 = 'link_down1.png'
Player_down2 = 'link_down2.png'


# Maps
Maps = 'Map_infinite.tmx'
Castle_map = 'Map.tmx'

# Music
BG_music = 'Meeting Place NES.wav'


