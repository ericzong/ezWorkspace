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
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        str_len = len(s)
        for i in range(0, str_len):
            c = s[i]
            start = i
            end = str_len
            while (idx := s.rfind(c, start, end)) > start:
                part = s[i: idx + 1]
                if idx > i and self.is_palindrome(part) and len(part) > len(result):
                    result = part
                end = idx
        return result

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEqual("a", Solution5().longestPalindrome("a"))

    def test_case2(self):
        self.assertEqual("abcba", Solution5().longestPalindrome("abcbabac"))

    def test_case3(self):
        self.assertEqual("23432", Solution5().longestPalindrome("ccaba1123432cc"))

    def test_case4(self):
        self.assertEqual("bb", Solution5().longestPalindrome("cbbd"))

    def test_case5(self):
        self.assertEqual("bab", Solution5().longestPalindrome("babad"))


if __name__ == '__main__':
    unittest.main()
