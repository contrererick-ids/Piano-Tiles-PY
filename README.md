"""
# Piano-Tiles-PY
# Architecture: Layered (N-Tier)

Project Structure:
------------------
piano_tiles_project/
├── assets/                  # PM (Isaac V): Sounds, Fonts, Images
│   ├── sounds/
│   └── fonts/
├── src/
│   ├── main.py              # Entry point (Isaac V)
│   ├── infrastructure/      # PM (Isaac V): Config, Constants, Asset Loader
│   │   ├── settings.py
│   │   └── asset_manager.py
│   ├── presentation/        # Dev A (Erick C): PyGame Drawing, UI, Screens
│   │   ├── renderer.py
│   │   └── ui_components.py
│   ├── logic/               # Dev B (Nico G): Tile Math, Scoring, Game State
│   │   ├── tile_manager.py
│   │   └── engine.py
│   └── input/               # Dev C (Josue L): Event Handling, Input Mapping
│       └── event_handler.py
├── tests/                   # Dev D (Jorge V): Unit tests for each layer
└── requirements.txt
"""
