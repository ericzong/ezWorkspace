import unittest


class MyTestCase(unittest.TestCase):
    def test_r(self):
        my_color = Color(199, 237, 204)
        print(f"{my_color!r}")  # 调用 __repr__
        print(f"{my_color!s}")  # 调用 __str__
        print(f"{my_color}")    # 调用 __format__，默认分支
        print(f"{my_color:web}") # 调用 __format__，format_spec == web 分支


class Color:
    def __init__(self, red: int = 255, green: int = 255, blue: int = 255):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"Red:{self.red}, Green:{self.green}, Blue:{self.blue}"

    def __str__(self):
        return f"({self.red}, {self.green}, {self.blue})"

    def __format__(self, format_spec):
        if format_spec == "web":
            return f"#{self.red:02X}{self.green:02X}{self.blue:02X}"
        else:
            return f"R:{self.red}, G:{self.green}, B:{self.blue}"


if __name__ == '__main__':
    unittest.main()
