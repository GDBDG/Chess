# Run pylint inside th project (test if the code respect all sorts of conventions)
# R0903 : not enough public methods in class
# W0212 : Access to a protected member (reason : for the tests)
# R0801 : Similar code (reason : queen)
echo "==================================="
echo "Run pylint"
poetry run pylint --disable=R0903,R0801,W0212 ./app