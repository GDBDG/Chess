# run pytest, generate coverage report and open it in navigator
poetry run pytest --cov ./app/src
coverage html
open htmlcov/index.html