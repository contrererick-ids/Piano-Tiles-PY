import pygame
from tile_manager import TileManager


class GameEngine:
    def __init__(self, width=400, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Piano Tiles")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        self.tile_manager = TileManager(width, height)

    def run(self):
        while self.running:
            self.clock.tick(60)

            self.handle_events()

            if not self.game_over:
                self.update()

            self.draw()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                try:
                    self.tile_manager.handle_click(event.pos)
                except:
                    self.game_over = True

    def update(self):
        try:
            self.tile_manager.update()
        except:
            self.game_over = True


