# run pytest, generate coverage report and open it in navigator
evho "==================================="
echo "Run pytest, with coverage analysis"
poetry run pytest --cov ./app/src
echo "Build html report"
coverage html
echo "Open the report in web browser"
open htmlcov/index.html