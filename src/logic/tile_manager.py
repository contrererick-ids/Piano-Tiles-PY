import random
from src.infrastructure.settings import WIDTH, HEIGHT, TILE_WIDTH, TILE_HEIGHT, INITIAL_SPEED

class Tile:
    def __init__(self, lane, y):
        self.lane = lane
        self.x = lane * TILE_WIDTH
        self.y = y
        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT
        self.active = True # True = Black (clickable), False = Gray (clicked)

    def move(self, speed):
        self.y += speed

    def is_off_screen(self):
        return self.y > HEIGHT

class TileManager:
    def __init__(self):
        self.tiles = []
        self.speed = INITIAL_SPEED
        self.last_lane = -1
        self.spawn_y = -TILE_HEIGHT  # Start spawning just above screen
        
        # Fill screen with initial tiles
        self._fill_initial_tiles()

    def _fill_initial_tiles(self):
        # Create a few tiles to start with
        current_y = HEIGHT - TILE_HEIGHT * 2 # Start from bottom-ish
        while current_y > -TILE_HEIGHT * 2:
            self.spawn_tile(current_y)
            current_y -= TILE_HEIGHT

    def spawn_tile(self, y):
        available_lanes = [i for i in range(4) if i != self.last_lane]
        lane = random.choice(available_lanes)
        self.last_lane = lane
        
        tile = Tile(lane, y)
        self.tiles.append(tile)

    def update(self):
        # Move tiles
        for tile in self.tiles:
            tile.move(self.speed)

        # Remove off-screen tiles
        # If an active tile goes off screen, it's a Game Over
        tiles_to_remove = []
        missed_active_tile = False
        
        for tile in self.tiles:
            if tile.is_off_screen():
                if tile.active:
                    missed_active_tile = True
                tiles_to_remove.append(tile)
        
        for tile in tiles_to_remove:
            self.tiles.remove(tile)

        # Spawn new tiles
        if not self.tiles:
            self.spawn_tile(-TILE_HEIGHT)
        else:
            # Find the highest tile (smallest y)
            highest_tile = min(self.tiles, key=lambda t: t.y)
            if highest_tile.y > -TILE_HEIGHT:
                self.spawn_tile(highest_tile.y - TILE_HEIGHT)
                
        return missed_active_tile

    def check_click(self, pos):
        x, y = pos
        
        # Check if clicked on a tile
        for tile in self.tiles:
            if (tile.x <= x < tile.x + tile.width and 
                tile.y <= y < tile.y + tile.height):
                
                if tile.active:
                    tile.active = False
                    return "hit"
                else:
                    return "ignore" # Clicked already pressed tile
        
        return "miss" # Clicked empty space (white tile)

    def increase_speed(self):
        self.speed += 0.05
