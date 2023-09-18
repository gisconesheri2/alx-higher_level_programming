#!/usr/bin/python3
"""Model for a Square Object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class inherits from the Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialiaze the Square intance
        Args:
            size (int > 0) - dimensions of the square
            x (int >= 0) - used yo display the square
            y (int >= 0) - used to display the square
            id (int) - from Base class
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """getter method for size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter and validator for the size attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """overide Rectangle's __str__ method"""
        return (f"[{self.__class__.__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        if args in not empty, disregard kwargs
        args assigns(id, size, x, y) in that order
        """
        if args is not None and len(args) >= 1:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id, self.size = args[0], args[1]
            if len(args) == 3:
                self.id, self.size = args[0], args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id, self.size = args[0], args[1]
                self.x, self.y = args[2], args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    elif key == 'id':
                        self.id = value

    def to_dictionary(self):
        """returns a dictionary representation of a Square"""
        class_dict = {}
        class_dict['id'] = self.id
        class_dict['size'] = self.size
        class_dict['x'] = self.x
        class_dict['y'] = self.y
        return (class_dict)
