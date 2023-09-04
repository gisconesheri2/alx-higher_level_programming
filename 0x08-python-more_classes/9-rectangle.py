#!/usr/bin/python3

"""Models a rectangle
"""


class Rectangle:
    """models a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize the object
        Args:
            width (int): width of rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute
        Args:
            value (int): value supplied for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the width attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for width attribute
        Args:
            value (int): value supplied for width
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """calculates and returns the pereimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return (0)
        else:
            return ((self.width * 2) + (self.height * 2))

    def __del__(self):
        """prints to stdout to show object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """return object representation of the current rectangle"""
        return (f"Rectangle({self.width}, {self.height})")

    def __str__(self):
        """prints the rectangle with a '#' """
        if self.height == 0 or self.width == 0:
            return ()
        for row in range(self.height):
            for column in range(self.width):
                print(f"{self.print_symbol}", end="")
            if row == self.height - 1:
                continue
            print()
        return ("")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares the areas of two instances of Rectangle
        Args:
            rect_1 (Rectangle): Rectangle instance
            rect_2 (Rectangle): Rectangle instance
        Returns:
            the bigger Rectangle instance or the first instance
            if both rectangles are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
