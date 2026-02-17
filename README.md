# Piano-Tiles-PY

piano_tiles_project/
├── assets/                  # Managed by PM (Sounds, Fonts, Images)
│   ├── sounds/
│   └── fonts/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point (Managed by PM) (Isaac V)
│   ├── infrastructure/      # PM: Config, Constants, Asset Loader
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
