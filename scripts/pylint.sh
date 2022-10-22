# Run pylint inside th project (test if the code respect all sorts of conventions)
# R0903 : not enough public methods in classes (for Board, Square and moves)
# W0212 : Access to a protected member (reason : for the tests)
# CO123 : use isinstance rather than type (reason : not pertinent)
# C0103 : local disable bug, necessary in test to mock private attributes
echo "==================================="
echo "Run pylint"
poetry run pylint --disable=R0903,R0801,W0212,C0123,C0103 ./app