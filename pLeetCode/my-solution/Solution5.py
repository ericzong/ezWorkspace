import unittest

"""
【最长回文子串】
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""


class Solution5:
    def longest_palindrome(self, s: str) -> str:
        result = s[0]  # 默认取第一个字符为最长回文子串
        str_len = len(s)
        for i in range(0, str_len):
            c = s[i]  # 当前子串的首字符
            start = i  # 开始位置
            end = str_len  # 结束位置，默认为整个字符串
            while (idx := s.rfind(c, start, end)) > start:  # 在起止区间中查找与当前首字符相同的字符位置
                part = s[i: idx + 1]  # 截取起止字符相同的子串
                # 如果截取的子串是回文串，且长度比当前记录的结果长，则覆盖当前结果
                if idx > i and self.is_palindrome(part) and len(part) > len(result):
                    result = part
                    break  # 性能提升：从大范围搜索得到的子串，必然比从小范围搜索得到的子串长，就不用继续循环了
                end = idx  # 缩小搜索范围
        return result

    @staticmethod
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]


class MyTestCase(unittest.TestCase):
    def test_case0(self):
        self.assertEqual("666666", Solution5().longest_palindrome("666666999"))
    def test_case1(self):
        self.assertEqual("a", Solution5().longest_palindrome("a"))

    def test_case2(self):
        self.assertEqual("abcba", Solution5().longest_palindrome("abcbabac"))

    def test_case3(self):
        self.assertEqual("23432", Solution5().longest_palindrome("ccaba1123432cc"))

    def test_case4(self):
        self.assertEqual("bb", Solution5().longest_palindrome("cbbd"))

    def test_case5(self):
        self.assertEqual("bab", Solution5().longest_palindrome("babad"))


if __name__ == '__main__':
    unittest.main()
