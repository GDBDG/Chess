# run pytest, generate coverage report and open it in navigator
echo "==================================="
echo "Run pytest, with coverage analysis"
poetry run pytest --cov ./src/CHESS
echo "Build html report"
coverage html
echo "Open the report in web browser"
open htmlcov/index.html