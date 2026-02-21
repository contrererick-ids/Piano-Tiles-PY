from src.logic.tile_manager import TileManager

class GameEngine:
    def __init__(self):
        self.tile_manager = TileManager()
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return

        missed = self.tile_manager.update()
        if missed:
            self.game_over = True

    def handle_click(self, pos):
        if self.game_over:
            return None

        result = self.tile_manager.check_click(pos)
        
        if result == "hit":
            self.score += 1
            if self.score % 10 == 0:
                self.tile_manager.increase_speed()
            return "hit"

        elif result == "miss":
            self.game_over = True
            return "miss"
            
        elif result == "ignore":
            return "ignore"
            
        return None

    def get_tiles(self):
        return self.tile_manager.tiles
    
    def get_score(self):
        return self.score
