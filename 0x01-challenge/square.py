#!/usr/bin/python3
""" class square"""


class Square:
    """documentation"""

    def __init__(self, width):
        """documentation"""
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PerimiterOfMySquare(self):
        """perimeter of the square"""
        return 4 * self.width

    def __str__(self):
        """documentation"""
        return f"Square(width={self.width})"


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimiterOfMySquare())
