import pygame
from src.infrastructure.settings import (
    COLOR_WHITE, COLOR_BLACK, COLOR_GRAY, COLOR_RED,
    WIDTH, HEIGHT, TILE_WIDTH
)

class Renderer:

    # Instancias de screen y font de pygames inicializadas
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font

    # Background
    def draw_background(self) -> None:
        # Rellena el fondo de un color pasado por parametro, en este caso una variable global COLOR_WHITE
        self.screen.fill(COLOR_WHITE)
        # Dibuja una línea con el método draw.line de pygame
        for i in range(1, 4):
            x = TILE_WIDTH * i
            pygame.draw.line(self.screen, COLOR_GRAY, (x, 0), (x, HEIGHT), 1)

    # Tiles
    def draw_tile(self, tile) -> None:
        if not tile.active:
            return
        # Rect genera y guarda las coordenadas de un rectangulo
        rect = pygame.Rect(tile.x + 2, tile.y, tile.width - 4, tile.height)
        # Dibuja un rectángulo pasado por parametro en una superficie tambien pasada como parametro
        pygame.draw.rect(self.screen, COLOR_BLACK, rect, border_radius=6)

    def draw_tiles(self, tiles: list) -> None:
        # Ciclo iterativo que manda a dibujar las "tiles" proporcionadas en la lista
        for tile in tiles:
            self.draw_tile(tile)

    # Text
    def draw_text(self, text: str, position: tuple, color: tuple = COLOR_BLACK, center: bool = False) -> None:
        # No existe un método que renderice un texto, entonces se renderiza una pantalla que contiene un texto
        surface = self.font.render(text, True, color)
        # Se obteiene el rectangulo de la pantalla que contiene el texto
        rect = surface.get_rect()
        # Si center es True, se coloca el rectangulo en la posicion pasada por parametro
        if center:
            rect.center = position
        # Si no, se ajusta el rectangulo para que su esquina superior izquierda inicie en el poaisicion
        else:
            rect.topleft = position
        # Sobreposiciona el nuevo rectangulo sobre la pantalla
        self.screen.blit(surface, rect)

    # Buttons
    def draw_button(self, rect: pygame.Rect, text: str, bg_color: tuple = COLOR_BLACK, text_color: tuple = COLOR_WHITE) -> None:
        # Dibuja un button que es un rectangulo pasado como parametro en la pantalla tambien pasada por parametro
        pygame.draw.rect(self.screen, bg_color, rect, border_radius=8)
        # Llamada a la funcion draw_text definida arriba
        self.draw_text(text, rect.center, color=text_color, center=True)

    # Score HUD
    def draw_score(self, score: int) -> None:
        # Llamada a la funcion draw_text pero este simplemente es el contador del puntaje presentado en pantalla
        self.draw_text(f"Score: {score}", (10, 10), color=COLOR_BLACK)

    # Images
    def draw_image(self, surface: pygame.Surface, position: tuple, center: bool = True) -> None:
        rect = surface.get_rect()
        if center:
            rect.center = position
        else:
            rect.topleft = position
        self.screen.blit(surface, rect)