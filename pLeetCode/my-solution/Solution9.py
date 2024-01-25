import math
import unittest

"""
【回文数】
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
"""


class Solution9:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        """
        进阶-反转一半数字
        """
        # 排除特殊场景：
        # 1. 负数不是回文数
        # 2. 个位为 0 的数不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_no = 0  # 存储后一半数字串（逆序）
        while x > reverted_no:
            # 退出场景：
            # 1. x 与 reverted_no 位数相同，相等即为回文
            # 2. x 比 reverted_no 少一位，reverted_no 个位即中间数字，舍弃该位后相等，则为回文
            reverted_no = reverted_no * 10 + x % 10
            x //= 10
        return x == reverted_no or x == reverted_no // 10

    @staticmethod
    def is_palindrome_2(x: int) -> bool:
        """
        定义解法优化：分别翻转前后一半，相同即为“回文”
        时间复杂度：o(log10(n))
        空间复杂度：O(1)
        """
        xstr = str(x)
        h = len(xstr) // 2
        return xstr[: h] == xstr[-1:-h - 1:-1]

    @staticmethod
    def is_palindrome_1(x: int) -> bool:
        """
        定义解法：将数字视为字符串，翻转后与自身相同，即为“回文”
        """
        xstr = str(x)
        return xstr == xstr[::-1]


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(Solution9.is_palindrome(121))

    def test_case2(self):
        self.assertFalse(Solution9.is_palindrome(-121))

    def test_case3(self):
        self.assertFalse(Solution9.is_palindrome(10))

    def test_case4(self):
        self.assertTrue(Solution9.is_palindrome(11))


if __name__ == '__main__':
    unittest.main()
