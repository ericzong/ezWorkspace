import unittest

import jsonpath

json_data = {
    "name": "张三",
    "age": 22,
    "address": {
        "province": "深圳",
        "district": "福田"
    },
    "phoneNumbers": [
        {
            "type": "mobile",
            "number": "+86-12345678912"
        },
        {
            "type": "office",
            "number": "0755-12345678"
        }
    ]
}


class MyTestCase(unittest.TestCase):
    # 数组下标
    def test_case1(self):
        data = jsonpath.jsonpath(json_data, '$.phoneNumbers[1].number')
        self.assertEqual(data, ["0755-12345678"])

    # * 的使用
    def test_case2(self):
        data = jsonpath.jsonpath(json_data, '$.phoneNumbers[*].number')
        self.assertEqual(data, ["+86-12345678912", "0755-12345678"])

    # 切片
    def test_case3(self):
        data = jsonpath.jsonpath(json_data, '$.phoneNumbers[0,1].number')
        self.assertEqual(data, ["+86-12345678912", "0755-12345678"])


if __name__ == '__main__':
    unittest.main()
