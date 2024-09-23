# jsonpath_ng v1.6.1
from jsonpath_ng.ext import parse

json_data = {
    "store": {
        "book": [
            {"category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "price": 22.99},
            {"category": "fiction", "author": "J  K. Rowling", "title": "Harry Potter", "price": 19.99},
            {"category": "nonfiction", "author": "Robert C. Martin", "title": "Clean Code", "price": 14.95}
        ]
    }
}

jsonpath_expr = parse("$.store.book[*].(author + ' - ' + title)")
result = [match.value for match in jsonpath_expr.find(json_data)]
print(result)