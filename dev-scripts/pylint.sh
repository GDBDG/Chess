# Run pylint inside th project (test if the code respect all sorts of conventions)
# R0903 : not enough public methods in class
poetry run pylint --disable=R0903 ./app