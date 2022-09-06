"""Constants of the project"""
from pathlib import Path

# Absolute path for app
PROJECT_DIR = next(p for p in Path(__file__).parents if p.name == "app")
