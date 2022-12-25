"""Constants of the project"""
from pathlib import Path

# Absolute path for app
SOURCE_DIR = next(p for p in Path(__file__).parents if p.name == "src")

UI_FILES_DIR = SOURCE_DIR / "ui"
