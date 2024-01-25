import csv
import json
import unittest


def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

        # 获取所有键
        keys = list(data.keys())

        # 获取所有值
        values = list(data.values())

        # 将键和值写入 CSV 文件
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['key', 'value'])  # 写入列标题
            writer.writerows(zip(keys, values))  # 写入键值对


the_json_file = 'en.json'
the_csv_file = 'en.csv'


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        convert_json_to_csv(the_json_file, the_csv_file)


if __name__ == '__main__':
    unittest.main()
