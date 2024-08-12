import unittest

"""
哈沙德数
如果一个整数能够被其各个数位上的数字之和整除，则称之为 哈沙德数（Harshad number）。
给你一个整数 x 。如果 x 是 哈沙德数 ，则返回 x 各个数位上的数字之和，否则，返回 -1 。

示例 1：
输入： x = 18
输出： 9
解释：
x 各个数位上的数字之和为 9 。18 能被 9 整除。因此 18 是哈沙德数，答案是 9 。

示例 2：
输入： x = 23
输出： -1
解释：
x 各个数位上的数字之和为 5 。23 不能被 5 整除。因此 23 不是哈沙德数，答案是 -1 。

提示：
1 <= x <= 100
"""
class Solution3099:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_no = 0
        temp_no = x

        while temp_no:
            temp_no, current_no = divmod(temp_no, 10)
        # while temp_no > 9 :
            # current_no = temp_no % 10
            # temp_no //= 10
            sum_no += current_no
        # else:
        #     sum_no += temp_no

        return -1 if x % sum_no else sum_no

class MyTestCase(unittest.TestCase):

    def test_case1(self):
        result = Solution3099().sumOfTheDigitsOfHarshadNumber(18)
        self.assertEqual(result, 9)

    def test_case2(self):
        result = Solution3099().sumOfTheDigitsOfHarshadNumber(23)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
