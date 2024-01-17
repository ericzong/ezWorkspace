import datetime
import time
import unittest

import arrow
import pytz as pytz

the_timestamp = 1704090905  # 时间戳
the_time_str = '2024-01-01 14:35:05'  # 对应的北京时间
the_time_formatter = '%Y-%m-%d %H:%M:%S'
the_time_formatter2 = 'YYYY-MM-DD HH:mm:ss'
the_time_zone = pytz.timezone('Asia/Shanghai')


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        dt = datetime.datetime.fromtimestamp(the_timestamp)
        dt.replace(tzinfo=the_time_zone)
        time_str = dt.strftime(the_time_formatter)
        self.assertEqual(time_str, the_time_str)

    def test_case2(self):
        # time.timezone 是只读的，不能用于改变时区
        # 据查，time 包只能获取 UTC 时间以及本地时间，无法直接设置时区
        dt = time.localtime(the_timestamp)
        time_str = time.strftime(the_time_formatter, dt)
        self.assertEqual(time_str, the_time_str)

    def test_case3(self):
        dt = arrow.get(the_timestamp, tzinfo=the_time_zone)
        # dt = dt.to(tz=the_time_zone)
        time_str = dt.format(the_time_formatter2)
        self.assertEqual(time_str, the_time_str)


if __name__ == '__main__':
    unittest.main()
