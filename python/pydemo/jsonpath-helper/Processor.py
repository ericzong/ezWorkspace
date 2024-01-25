import unittest

from jsonpath_ng import parse

json_obj = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}


class JsonpathTestCase(unittest.TestCase):
    # 提取单个属性的值
    @staticmethod
    def test_case1():
        jsonpath_expr = parse('$.store.book[0].title')
        result = [match.value for match in jsonpath_expr.find(json_obj)]
        assert result[0] == "Sayings of the Century"

    # 提取数组中的所有元素
    @staticmethod
    def test_case2():
        jsonpath_expr = parse("$.store.book[*].author")
        result = [match.value for match in jsonpath_expr.find(json_obj)]
        assert result == ["Nigel Rees", "Evelyn Waugh"]

    # 提取满足条件的元素
    # @staticmethod
    # def test_case3():
    #     jsonpath_expr = parse("$.store.book[?(@.price < 10)].title")
    #     result = [match.value for match in jsonpath_expr.find(json_obj)]
    #     assert result == ["Sayings of the Century"]

    # 提取嵌套属性的值
    @staticmethod
    def test_case4():
        jsonpath_expr = parse("$.store.bicycle.color")
        result = [match.value for match in jsonpath_expr.find(json_obj)]
        assert result[0] == "red"

    # 提取多个属性的值并进行组合
    # @staticmethod
    # def test_case5():
    #     jsonpath_expr = parse("$.store.book[0].['title', 'author']")
    #     result = [match.value for match in jsonpath_expr.find(json_obj)]
    #     assert result[0] == {"title": "Sayings of the Century", "author": "Nigel Rees"}


if __name__ == '__main__':
    unittest.main()
