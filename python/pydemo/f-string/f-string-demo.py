import unittest


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_r():
        my_color = Color(199, 237, 204)
        print(f"{my_color!r}")  # 调用 __repr__
        print(f"{my_color!s}")  # 调用 __str__
        print(f"{my_color!a}")  # 调用 __repr__，将结果中的非 ASCII 字符转义为 ASCII 转义序列
        print(ascii(my_color.__repr__()))  # 跟 !a 有差异，结果会用引号括起来
        print(f"{my_color}")  # 调用 __format__，默认分支
        print(f"{my_color:web}")  # 调用 __format__，format_spec == web 分支


class Color:
    def __init__(self, red: int = 255, green: int = 255, blue: int = 255):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"红: {self.red}, 绿: {self.green}, 蓝: {self.blue}"

    def __str__(self):
        return f"({self.red}, {self.green}, {self.blue})"

    def __format__(self, format_spec):
        if format_spec == "web":
            return f"#{self.red:02X}{self.green:02X}{self.blue:02X}"
        else:
            return f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}"


if __name__ == '__main__':
    unittest.main()
