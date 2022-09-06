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

## Implemented rules

I made the choice to use the [threefold repetition rule](https://en.wikipedia.org/wiki/Threefold_repetition) 
automatically, like the chess.com app.
That means the player doesn't have to claim
the draw after 3 repetitions, it will be done automatically, and makes the fivefold repetition rule useless.

I also made the choice to use the [fifty-move rule](https://en.wikipedia.org/wiki/Fifty-move_rule#Seventy-five-move_rule).
