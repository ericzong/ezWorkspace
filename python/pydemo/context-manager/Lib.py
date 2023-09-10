from contextlib import contextmanager


@contextmanager
def context():
    """
    使用 contextlib 库简化上下文管理器实现：用到了 @contextmanager 装饰器和 yield
    :return:
    """
    print("enter...")  # yield 之前，在 __enter__ 中执行
    yield 'VALUE'  # 该值会赋值给 as 子句标识符
    print("exit...")   # yield 之后，在 __exit__ 中执行


with context() as val:
    print("run...")
    print(val)
