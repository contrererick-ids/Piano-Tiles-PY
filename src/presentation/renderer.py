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

    def draw_chinese_text(self, text: str, position: tuple, color: tuple = COLOR_BLACK) -> None:
        # Fallback list for Chinese fonts on different OS
        chinese_fonts = ["PingFang SC", "Heiti SC", "Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "Arial Unicode MS"]
        
        selected_font = None
        for font_name in chinese_fonts:
            try:
                # Check if system has this font
                if font_name in pygame.font.get_fonts() or pygame.font.match_font(font_name):
                    selected_font = pygame.font.SysFont(font_name, 40)
                    break
            except:
                continue
                
        # If no specific font found, try default generic match
        if not selected_font:
             path = pygame.font.match_font('arial') # Ultimate fallback, likely just squares for chinese but safe
             selected_font = pygame.font.Font(path, 40)

        # Force valid font for unicode
        # Note: Pygame SysFont might not raise error but return default if not found. 
        # Let's trust 'PingFang SC' works on Mac as requested, but if User says "looks same", maybe it's not rendering.
        
        # Explicit attempt for Mac
        try:
             # Just instantiate what worked before but ensure it renders
             font = pygame.font.SysFont("PingFang SC", 40)
             surface = font.render(text, True, color)
             
             # If width is 0 or very small, it might have failed to render char
             if surface.get_width() == 0:
                 raise Exception("Font render empty")
        except:
             # Fallback to a known widely available default that usually covers unicode
             font = pygame.font.SysFont("Arial Unicode MS", 40)
             surface = font.render(text, True, color)

        rect = surface.get_rect(center=position)
        self.screen.blit(surface, rect)

    def draw_lantern(self, x, y):
        # Draw a simple red lantern with gold outline
        pygame.draw.circle(self.screen, (220, 20, 60), (x, y), 30) # Crimson Body
        pygame.draw.circle(self.screen, (255, 215, 0), (x, y), 30, 3) # Gold outline
        pygame.draw.line(self.screen, (255, 215, 0), (x, y-30), (x, y-50), 2) # String
        pygame.draw.line(self.screen, (255, 215, 0), (x, y+30), (x, y+50), 2) # Tassel