# Run pylint inside th project (test if the code respect all sorts of conventions)
# R0903 : not enough public methods in class
# R0904 : too many public methods in class
# W0212 : Access to a protected member (reason : for the tests)
echo "==================================="
echo "Run pylint"
poetry run pylint --disable=R0903,R0904,W0212 ./app