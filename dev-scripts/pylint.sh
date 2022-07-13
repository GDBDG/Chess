# Run pylint inside th project (test if the code respect all sorts of conventions)
# R0903 : not enough public methods in class (for Board, Square and move)
# W0212 : Access to a protected member (reason : for the tests)
# R0801 : Similar code (reason : queen)
# C0415 : import outside top level (reason : Move and Pawn, avoid cyclic imports problems)
# R0401 : cyclic import (reason : Move and Pawn)
echo "==================================="
echo "Run pylint"
poetry run pylint --disable=R0903,R0801,W0212,C0415,R0401 ./app