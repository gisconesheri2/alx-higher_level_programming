#!/usr/bin/python3
"""test suite for Rectangle Class"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """test the Rectangle class"""

    def test_getter_methods(self):
        """test getter methods"""
        # provide all arguments
        r1 = Rectangle(10, 20, 2, 3, 23)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 23)

        # provide only required arguments
        r2 = Rectangle(10, 20)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_setter_methods(self):
        """test setter methods work"""
        r3 = Rectangle(12, 23)
        r3.width = 13
        r3.height = 78
        r3.x = 34
        r3.y = 43
        self.assertEqual(r3.width, 13)
        self.assertEqual(r3.height, 78)
        self.assertEqual(r3.x, 34)
        self.assertEqual(r3.y, 43)

    def test_not_ints(self):
        """test TypeError raised when values passed are not ints"""

        with self.assertRaises(TypeError):
            r4 = Rectangle('3', 4)
        with self.assertRaises(TypeError):
            r4 = Rectangle(3, True)
        with self.assertRaises(TypeError):
            r4 = Rectangle(3, 4, [1, 2, 3], 2)
        with self.assertRaises(TypeError):
            r4 = Rectangle(3, 4, 2, (2, 3))

    def test_negative_nums(self):
        """test ValueError is raised on values less than 0"""

        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-3, 3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(3, -7)
        with self.assertRaises(ValueError):
            r4 = Rectangle(3, 3, -4, 3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(3, 3, 3, -4)

        r4 = Rectangle(3, 4, 0, 0)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_area_method(self):
        """test the area method"""
        r6 = Rectangle(3, 4)
        self.assertEqual(r6.area(), 12)
        r7 = Rectangle(5, 6)
        self.assertEqual(r7.area(), 30)

    def test_str_method(self):
        """test the str method"""
        r8 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r8.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r9 = Rectangle(5, 5, 1, id=1)
        self.assertEqual(r9.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_method(self):
        """test update method"""
        r10 = Rectangle(10, 10, 10, 10, 2)
        self.assertEqual(r10.__str__(), "[Rectangle] (2) 10/10 - 10/10")
        r10.update()
        self.assertEqual(r10.__str__(), "[Rectangle] (2) 10/10 - 10/10")
        r10.update(89, 2, 3, 4, 5)
        self.assertEqual(r10.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r10.update(89, 14, 45)
        self.assertEqual(r10.__str__(), "[Rectangle] (89) 4/5 - 14/45")
        with self.assertRaises(ValueError):
            r10.update(89, 0)

    def test_update_with_kwargs(self):
        """test updated update method to handle Kwargs"""
        r11 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r11.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r11.update()
        self.assertEqual(r11.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r11.update(89)
        self.assertEqual(r11.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r11.update(89, 2)
        self.assertEqual(r11.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r11.update(height=89, y=33, x=2)
        self.assertEqual(r11.__str__(), "[Rectangle] (89) 2/33 - 2/89")
        r11.update(1000, y=45667, x=5454546, height=6777)
        self.assertEqual(r11.__str__(), "[Rectangle] (1000) 2/33 - 2/89")
        r11.update(width=20, y=20, x=20, height=20, id=20)
        self.assertEqual(r11.__str__(), "[Rectangle] (20) 20/20 - 20/20")
        r11.update(40, 40, 40, 40, 40)
        self.assertEqual(r11.__str__(), "[Rectangle] (40) 40/40 - 40/40")

    def test_to_dictionary(self):
        """test the to_dictionary method"""

        r12 = Rectangle(10, 2, 1, 9, 2)
        r12_dict = r12.to_dictionary()
        self.assertEqual(r12_dict['width'], 10)
        self.assertEqual(r12_dict['height'], 2)
        self.assertEqual(r12_dict['x'], 1)
        self.assertEqual(r12_dict['y'], 9)
        self.assertEqual(r12_dict['id'], 2)

        r13 = Rectangle(1, 1)
        r13.update(**r12_dict)
        self.assertEqual(r13.__str__(), "[Rectangle] (2) 1/9 - 10/2")

    def test_to_json_string(self):
        """tests that a JSON string is generated from a python dict"""
        r14 = Rectangle(10, 7, 2, 8, 2)
        dict_1 = r14.to_dictionary()

        json_dictionary = Base.to_json_string([dict_1])
        self.assertTrue(type(json_dictionary) is str)

    def test_load_from_file(self):
        """test the serialization and deserialization of Base objects
        tests three methods:
            save_t0_file(ist_objs) - writes JSON string of list_objs to file
            from_json_string(json_string) - gets a python object from
            JSON string
            create(**dictionary) - makes a new instance of a Base object
            from the values in the dictionary
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        lro = Rectangle.load_from_file()
        self.assertEqual(lro[0].__str__(), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(lro[1].__str__(), "[Rectangle] (2) 0/0 - 2/4")
        self.assertFalse(r1 == lro[0])
        self.assertFalse(r2 == lro[1])
