# Piano-Tiles-PY

## Architecture: Layered (N-Tier)

This project implements a Piano Tiles clone using a decoupled, layered architecture to ensure separation of concerns and maintainability.

### Project Structure

```text
piano_tiles_project/
├── assets/                  # PM (Isaac V): Sounds, Fonts, Images
│   ├── sounds/
│   └── fonts/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point (Isaac V)
│   ├── infrastructure/      # PM (Isaac V): Config, Constants, Asset Loader
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── asset_manager.py
│   ├── presentation/        # Dev A (Erick C): PyGame Drawing, UI, Screens
│   │   ├── __init__.py
│   │   ├── renderer.py
│   │   └── ui_components.py
│   ├── logic/               # Dev B (Nico G): Tile Math, Scoring, Game State
│   │   ├── __init__.py
│   │   ├── tile_manager.py
│   │   └── engine.py
│   └── input/               # Dev C (Josue L): Event Handling, Input Mapping
│       ├── __init__.py
│       └── event_handler.py
├── tests/                   # Dev D (Jorge V): Unit tests for each layer
└── requirements.txt

## How to Run

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python src/main.py
   ```
