#!/usr/bin/python3
"""a Rectangle Class that models a rectangle"""
from models.base import Base


class Rectangle(Base):
    """a model of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise a Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter and validator for the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter and validator for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """setter and validator for the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for width attribute"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """setter and validator for the height attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate and return the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints the rectangle instance with character #
        the y value pushes the rows downwards and x pushes
        the coulmns to the right"""
        for line_space in range(self.y):
            print()
        for row in range(self.height):
            for ln in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        if args in not empty, disregard kwargs
        args assigns(id, width, height, x, y) in that order
        """
        if args is not None and len(args) >= 1:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id, self.width = args[0], args[1]
            if len(args) == 3:
                self.id, self.width, self.height = args[0], args[1], args[2]
            if len(args) == 4:
                self.id, self.width, self.height = args[0], args[1], args[2]
                self.x = args[3]
            if len(args) == 5:
                self.id, self.width, self.height = args[0], args[1], args[2]
                self.x, self.y = args[3], args[4]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    elif key == 'id':
                        self.id = value

    def to_dictionary(self):
        """returns a dictionary representation of Rectangle"""
        class_dict = {}
        class_dict['id'] = self.id
        class_dict['width'] = self.width
        class_dict['height'] = self.height
        class_dict['x'] = self.x
        class_dict['y'] = self.y
        return (class_dict)

    def __str__(self):
        """implement the str magic method"""
        return(f"[{self.__class__.__name__}] ({self.id})"
               f" {self.x}/{self.y} - {self.width}/{self.height}")
