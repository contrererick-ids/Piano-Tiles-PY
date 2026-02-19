import os

import pygame


class AssetManager:
    def __init__(self):
        # Dictionaries to store loaded assets
        self.sounds = {}
        self.fonts = {}
        self.images = {}

        # Determine the base path for the assets folder
        # This points to the /src/assets folder
        self.base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../assets")
        )

    def load_assets(self):
        """Initializes and loads all game assets."""
        print(f"Loading assets from: {self.base_path}")

        # 1. Load Sounds
        # Usage: assets.sounds['tap'].play()
        self._load_sound("tap", "sounds/tap.wav")
        self._load_sound("game_over", "sounds/gameover.wav")
        
        # Load Music
        self.music_path = os.path.join(self.base_path, "sounds/song.mp3")

        # 2. Load Fonts
        # Usage: assets.fonts['score'].render("100", True, (0,0,0))
        # 2. Load Fonts
        # Usage: assets.fonts['score'].render("100", True, (0,0,0))
        self.fonts["score"] = pygame.font.SysFont("Arial", 32, bold=True)
        self.fonts["title"] = pygame.font.SysFont("Arial", 50, bold=True)
        # MacOS usually has PingFang SC. Fallback to common ones if needed.
        self.fonts["chinese"] = pygame.font.SysFont("PingFang SC", 40)

    def _load_sound(self, key, relative_path):
        full_path = os.path.join(self.base_path, relative_path)
        if os.path.exists(full_path):
            self.sounds[key] = pygame.mixer.Sound(full_path)
        else:
            print(f"Warning: Sound file not found at {full_path}")

    def play_sound(self, key):
        """Helper to play a sound by its key name."""
        if key in self.sounds:
            self.sounds[key].play()

    def play_music(self):
        if os.path.exists(self.music_path):
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1) # Loop indefinitely
        else:
            print(f"Warning: Music file not found at {self.music_path}")
