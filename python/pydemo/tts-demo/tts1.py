import unittest

import pyttsx3


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 初始化语音引擎
        engine = pyttsx3.init()

        # 让它说点什么
        engine.say("Hello, 这是一段Python代码让电脑开口说话的测试！")
        engine.runAndWait()  # 运行


if __name__ == '__main__':
    unittest.main()
