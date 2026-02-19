import pygame
from typing import Optional
from src.infrastructure.settings import WIDTH, HEIGHT, COLOR_BLACK, COLOR_WHITE, COLOR_RED
from src.presentation.renderer import Renderer

#Button layout (un rect de pygame) para que lo compartan las distintas clases (Menu, GameScreen y GameOver)
def _center_button(width: int = 200, height: int = 50, offset_y: int = 0) -> pygame.Rect:
    x = (WIDTH - width) // 2
    y = HEIGHT // 2 + offset_y
    return pygame.Rect(x, y, width, height)

# MenuScreen
class MenuScreen:

    # Start button
    _BTN_START = _center_button(offset_y=20)

    # Instancia de la clase Renderer
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    # Funcion para renderizar el Menu de Inicio
    def render(self) -> None:
        # Dibuja el fondo de la pantalla Menu
        self.renderer.draw_background()
        # Dibuja el texto (un rect) que muestra el titulo
        self.renderer.draw_text(
            "Piano Tiles",
            (WIDTH // 2, HEIGHT // 3),
            center=True,
        )
        # Dibuja el boton para comenzar
        self.renderer.draw_button(self._BTN_START, "Start")

    # Funcion que determina si el boton fue seleccionado para iniciar el juego
    def handle_click(self, pos: tuple) -> Optional[str]:
        if self._BTN_START.collidepoint(pos):
            return "start"
        return None


# GameScreen
class GameScreen:

    # Instancia de Renderer para la pantalla del juego en ejecucion
    def __init__(self, renderer: Renderer, engine):
        self.renderer = renderer
        self.engine = engine

    # Funcion para renderizar la pantalla del juego en ejecucion
    def render(self) -> None:
        # Dibuja el background
        self.renderer.draw_background()
        # Dibuja las "tiles"
        self.renderer.draw_tiles(self.engine.get_tiles())
        # Dibuja el score actual
        self.renderer.draw_score(self.engine.get_score())


# GameOverScreen
class GameOverScreen:

    # Botones de "Reinicio" y "Salida"
    _BTN_RESTART = _center_button(offset_y=20)
    _BTN_EXIT    = _center_button(offset_y=90)

    # Instancia de Renderer para la pantalla de finalizacion
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    # Funcion para renderizar la pantalla de finalizacion
    def render(self, score: int) -> None:
        # Dibuja el background
        self.renderer.draw_background()
        # Dibuja el titulo
        self.renderer.draw_text(
            "Game Over",
            (WIDTH // 2, HEIGHT // 3 - 30),
            color=COLOR_BLACK,
            center=True,
        )
        # Dibuja el puntaje obtenido
        self.renderer.draw_text(
            f"Score: {score}",
            (WIDTH // 2, HEIGHT // 3 + 20),
            color=COLOR_BLACK,
            center=True,
        )
        # Dibuja los botones para reiniciar o salir
        self.renderer.draw_button(self._BTN_RESTART, "Restart")
        self.renderer.draw_button(self._BTN_EXIT, "Exit", bg_color=COLOR_RED)

    # Funcion que determina si se reinicia el juego o se sale de la aplicacion
    def handle_click(self, pos: tuple) -> Optional[str]:
        # Checa el boton de "Reinicio"
        if self._BTN_RESTART.collidepoint(pos):
            return "restart"
        # Checa el boton de "Salida"
        if self._BTN_EXIT.collidepoint(pos):
            return "exit"
        return None