import pygame
import sys

from src.infrastructure.settings import WIDTH, HEIGHT
from src.presentation.renderer import Renderer
from src.presentation.ui_components import MenuScreen, GameScreen, GameOverScreen
from src.input.event_handler import EventHandler

class Board:
    def __init__(self):
        self.tiles = []

class Score:
    def get_score(self):
        return 0

# un controlador placeholder para probar
class Controller:
    def __init__(self):
        self.board = Board()
        self.score = Score()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32)

    renderer = Renderer(screen, font)
    event_handler = EventHandler()
    
    menu_screen = MenuScreen(renderer)
    game_screen = GameScreen(renderer, Controller())
    game_over_screen = GameOverScreen(renderer)

    current_state = "menu"
    running = True
    final_score = 0

    while running:
        for event in event_handler.get_events():

            if event_handler.is_quit(event):
                running = False

            click_pos = event_handler.get_click_pos(event)
            if click_pos:
                if current_state == "menu":
                    action = menu_screen.handle_click(click_pos)
                    if action == "start":
                        current_state = "game"

                elif current_state == "game":
                    # como aun no hay tiles cualquier click termina el juego
                    current_state = "game_over"

                elif current_state == "game_over":
                    action = game_over_screen.handle_click(click_pos)
                    if action == "restart":
                        current_state = "game"
                    elif action == "exit":
                        running = False

        if current_state == "menu":
            menu_screen.render()
        elif current_state == "game":
            game_screen.render()
        elif current_state == "game_over":
            game_over_screen.render(final_score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()