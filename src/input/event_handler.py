import pygame

class EventHandler:
    def get_events(self):
        return pygame.event.get()

    def is_quit(self, event) -> bool:
        return event.type == pygame.QUIT

    def get_click_pos(self, event) -> tuple | None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return event.pos # retorna el (x, y) del click
        return None

    def is_key_pressed(self, event, key) -> bool:
        return event.type == pygame.KEYDOWN and event.key == key