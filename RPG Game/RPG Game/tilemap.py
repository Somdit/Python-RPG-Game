import pygame
from settings import*
import pytmx

# *OLD*
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename,'rt') as f:
            for line in f:
                self.data.append(line.strip())
    
        # The tilemap width and height 
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        # Pixel
        self.width = self.tilewidth * Tile_size
        self.height = self.tileheight * Tile_size

 
class TiledMap:
    def __init__(self,filename):
        # Load file
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, screen_width, screen_height)
        self.width = width
        self.height = height

    # Apply to object
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(screen_width / 2)
        y = -target.rect.y + int(screen_height / 2)

        # limit camera scrolling
        x = min(0, x)
        x = max(-(self.width - screen_width), x)
        y = min(0, y)
        y = max(-(self.height - screen_height), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)

        