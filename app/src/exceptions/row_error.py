"""
row error
"""


class RowError(Exception):
    """
    Exception raised when row coordinates are not between 1 and 8
    """

    def __init__(self, row: int):
        """
        Builder of the error
        Create the error message
        @param row: problematic row (used for the error message)
        """
        self.row = row
        self.message = f"Row must be between 1 and 8, instead of {self.row}"
        super().__init__(self.message)

    def __str__(self):
        """
        str function
        @return: error message
        """
        return self.message
