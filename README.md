# Chess UI and AI

## Installations to dev the project
This project uses [poetry](https://python-poetry.org/docs/) to manage the packages, and uses python 3.9.

Use ```poetry install``` to install the project, and ```poetry run <cmd>``` to run command inside the poetry venv.

## Architecture of the project

* app : all project files (src + tests)
* app/src/back : backend of chess game (implement game rules and cie)
* exceptions : contains all customs exception
* dev-scripts : some useful scripts for dev (pytest, ...)
* .github/workflows : pipelines scripts