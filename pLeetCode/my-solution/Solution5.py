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
    def longest_palindrome0(self, s: str) -> str:
        """
        暴力解法一(完全枚举)

        思路：（双循环）枚举指定字符串所有子串，判断是否回文

        时间复杂度：O(n³)
        空间复杂度：O(n)
        """
        str_len = len(s)
        if str_len < 2:
            return s

        # 提升性能：不截取回文子串，只记录起始索引和长度
        max_len = 1  # 记录最长回文子串长度
        begin = 0  # 记录最长回文子串起始索引
        for i in range(str_len):
            for j in range(0, str_len):
                if j - i + 1 > max_len and Helper.valid_palindrome_substr(s, i, j):
                    max_len = j - i + 1
                    begin = i

        return s[begin: begin + max_len]

    def longest_palindrome1(self, s: str) -> str:
        """
        暴力解法二

        思路：（单循环）遍历字符串子串，判断首尾字符相同的子串是否为回文，并记录较长的回文字串，最终得到最长回文子串
        """
        str_len = len(s)
        if str_len < 2:
            return s

        # 提升性能：不截取回文子串，只记录起始索引和长度
        max_len = 1  # 记录最长回文子串长度
        begin = 0  # 记录最长回文子串起始索引
        for i in range(str_len):
            c = s[i]  # 当前子串的首字符
            end = str_len  # 结束位置，默认为整个字符串
            while (idx := s.rfind(c, i, end)) > i:  # 在起止区间中查找与当前首字符相同的字符位置
                # 如果长度比当前记录的结果长，且是回文串，则覆盖当前结果
                if idx - i + 1 > max_len and Helper.valid_palindrome_substr(s, i, idx):
                    max_len = idx - i + 1  # 计算并覆盖记录回文串长度
                    begin = i  # 覆盖回文串起始索引
                    break  # 性能提升：从大范围搜索得到的子串，必然比从小范围搜索得到的子串长，就不用继续循环了
                end = idx  # 缩小搜索范围
        return s[begin: begin + max_len]

    def longest_palindrome2(self, s: str) -> str:
        """
        中心扩散算法

        思路：遍历所有回文中心，扩展出每个中心的最长回文子串，从而得到最长回文子串

        时间复杂度：O(n²)
        空间复杂度：O(1)
        """
        str_len = len(s)
        if str_len < 2:
            return s

        start, end = 0, 0  # 初始默认回文子串起止索引
        for i in range(len(s) - 1):
            # 奇数长度子串扩展
            left1, right1 = Helper.expand_around_center(s, i, i)
            # 偶数长度子串扩展
            left2, right2 = Helper.expand_around_center(s, i, i + 1)
            # 不需要关注奇偶子串长度大小，都跟当前最长子串（start, end）比较即可
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def longest_palindrome3(self, s: str) -> str:
        """
        动态规划算法

        思路：逐列构造一个二维表（右上部分），行(i)列(j)对应的数据dp[i][j]表示s[i..j]是否为回文串。
        优点是可以使用已生成的数据：dp[i][j] = dp[i+1][j-1]

        时间复杂度：O(n²)
        空间复杂度：O(n²)
        """
        str_len = len(s)
        if str_len < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否为回文串
        # 初始化 n*n 二维表
        dp = [[None] * str_len for _ in range(str_len)]

        # 注意二维表的生成顺序：按列(j)生成。因为可能会参考前一列的结果。
        for j in range(1, str_len):  # 不需要参考对角线上的结果，所以列索引从 1 开始
            for i in range(0, j):  # 根据定义 i <= j，所以只需要生成二维表右上角部分
                if s[i] != s[j]:  # 两头字符不同，则不是回文串
                    dp[i][j] = False
                else:  # 两头字符相同
                    if j - i < 3:  # j - i + 1 < 4，即子串长度为[1, 3]，双端字符已经相同，则为回文串
                        dp[i][j] = True
                    else:  # 该子串是否为回文串与去除首尾字符后的子串是否为回文串
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin: begin + max_len]

    def longest_palindrome(self, s: str) -> str:
        """
        Manacher算法
        """
        str_len = len(s)
        if str_len < 2:
            return s

        start, end = 0, -1
        # 为统一奇偶数回文字符串，在首尾及字符间添加特殊字符间隔
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = Helper.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = Helper.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]

class Helper:
    @staticmethod
    def valid_palindrome_substr(s: str, left: int, right: int) -> bool:
        """
        判断指定字符串的子串是否是回文字符串
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def expand_around_center(s, left, right):
        """
        中心扩散法，给定字符串及中心点，扩散查找最大的回文子串
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # 注意退出条件达成时多执行了一次加减，所以返回时要做一次逆运算

    @staticmethod
    def expand(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2


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
