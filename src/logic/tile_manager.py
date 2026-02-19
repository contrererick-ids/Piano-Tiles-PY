import random
import pygame


class Tile:
    def __init__(self, column, y, width, height, speed):
        self.column = column
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.clicked = False

    @property
    def rect(self):
        return pygame.Rect(
            self.column * self.width,
            self.y,
            self.width,
            self.height
        )

    def update(self):
        self.y += self.speed

    def is_off_screen(self, screen_height):
        return self.y > screen_height


class TileManager:
    def __init__(self, screen_width, screen_height):
        self.columns = 4
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.tile_width = screen_width // self.columns
        self.tile_height = 150
        self.speed = 5

        self.tiles = []
        self.score = 0

        self.spawn_initial_tiles()


    def spawn_tile(self):
        column = random.randint(0, self.columns - 1)
        y = -self.tile_height
        tile = Tile(column, y, self.tile_width, self.tile_height, self.speed)
        self.tiles.append(tile)

    def spawn_initial_tiles(self):
        for i in range(5):
            column = random.randint(0, self.columns - 1)
            y = -i * self.tile_height
            tile = Tile(column, y, self.tile_width, self.tile_height, self.speed)
            self.tiles.append(tile)

    def update(self):
        for tile in self.tiles:
            tile.update()

        self.handle_off_screen()
        self.ensure_continuous_tiles()

    def handle_off_screen(self):
        for tile in self.tiles[:]:
            if tile.is_off_screen(self.screen_height):
                if not tile.clicked:
                    raise Exception("Game Over")
                self.tiles.remove(tile)

    def ensure_continuous_tiles(self):
        if len(self.tiles) == 0:
            self.spawn_tile()
        else:
            last_tile = self.tiles[-1]
            if last_tile.y >= 0:
                self.spawn_tile()

    def handle_click(self, mouse_pos):
        for tile in self.tiles:
            if tile.rect.collidepoint(mouse_pos):
                if not tile.clicked:
                    tile.clicked = True
                    self.score += 1
                    return True

        raise Exception("Game Over")
