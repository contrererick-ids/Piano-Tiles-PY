import pygame
import sys
import os

# Add project root to python path so 'src' module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.infrastructure.settings import WIDTH, HEIGHT
from src.infrastructure.assets_manager import AssetManager
from src.presentation.renderer import Renderer
from src.presentation.ui_components import MenuScreen, GameScreen, GameOverScreen
from src.input.event_handler import EventHandler
from src.logic.engine import GameEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Piano Tiles PY")
    clock = pygame.time.Clock()
    
    # Initialize Assets
    assets = AssetManager()
    assets.load_assets()
    assets.play_music()

    # Use fonts from assets
    # Renderer init expects a font object. Let's use the one from assets or create one if renderer expects it passed.
    # Renderer text drawing uses self.font.
    # We can pass assets.fonts['score'] as default or just create one like before.
    # The original main created a font. Let's use assets.fonts['score'] for consistency or keep it simple.
    # Original: font = pygame.font.SysFont("Arial", 32)
    # Assets: assets.fonts["score"]
    
    font = assets.fonts["score"]
    renderer = Renderer(screen, font)
    event_handler = EventHandler()
    
    # Components
    menu_screen = MenuScreen(renderer)
    game_over_screen = GameOverScreen(renderer)
    
    # Game State
    engine = GameEngine()
    game_screen = GameScreen(renderer, engine)

    current_state = "menu"
    running = True
    final_score = 0

    while running:
        # Event Handling
        for event in event_handler.get_events():
            if event_handler.is_quit(event):
                running = False

            click_pos = event_handler.get_click_pos(event)
            if click_pos:
                if current_state == "menu":
                    action = menu_screen.handle_click(click_pos)
                    if action == "start":
                        engine = GameEngine() # Reset engine
                        game_screen = GameScreen(renderer, engine)
                        assets.unpause_music()
                        current_state = "game"

                elif current_state == "game":
                    result = engine.handle_click(click_pos)
                    if result == "hit":
                        assets.play_sound("tap")
                    elif result == "miss":
                        assets.play_sound("game_over")
                        assets.pause_music()
                        final_score = engine.get_score()
                        current_state = "game_over"

                elif current_state == "game_over":
                    action = game_over_screen.handle_click(click_pos)
                    if action == "restart":
                        engine = GameEngine() # Reset engine
                        game_screen = GameScreen(renderer, engine)
                        assets.unpause_music()
                        current_state = "game"
                    elif action == "exit":
                        running = False

        # Game Logic Updates
        if current_state == "game":
            engine.update()
            if engine.game_over:
                if current_state != "game_over": # Prevent double trigger if clicked miss already handled
                    assets.play_sound("game_over")
                    assets.pause_music()
                    final_score = engine.get_score()
                    current_state = "game_over"

        # Rendering
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