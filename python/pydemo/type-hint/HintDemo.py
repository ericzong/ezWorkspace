from typing import List, Tuple, Dict
from typing import TypeVar
from typing import Union
from typing import Optional
from typing import Any
from typing import Callable
from typing import Protocol


class Person:
    def __init__(self, name: str):
        self.name = name


# Type Hint（类型注解）

def hi(name: str) -> str:
    return "Hello! " + name


h: str = hi('Eric')


def default_hi(name: str = "world") -> str:
    # 默认参数
    return "Hello! " + name


def hi_person(person: Person) -> str:
    # 自定义类型
    return "Hello! " + person.name


# 容器类型
ls: List[int] = [1, 2, 3]
tp: Tuple[str, ...] = ("a", "b", "c")  # 注意，元组元素数量是固定的，如不关注数量应用 ... 代表任意数量
dic: Dict[str, int] = {"a": 1, "b": 2, "c": 3}

# 内置容器类型
build_in_ls: list[int] = [1, 2, 3]
build_in_tp: tuple[str, ...] = ("a", "b", "c")
build_in_dic: dict[str, int] = {"a": 1, "b": 2, "c": 3}

# 类型别名
# 备注：嵌套类型部分结构不匹配，在变量赋值时并不会有提示
Config = list[dict[Person, list[int]]]
config: Config = [
    {Person("Eric"): [100, 100, 100]},
    {Person("Zong"): [100, 100, 100]}
]


def print_config(cfg: Config):
    print(cfg)


print(config)
print_config(config)


# 可变参数
def hi_everyone(*args: str):
    say = "Hello!"
    for n in args:
        say += " " + n

    return say


print(hi_everyone('Eric', 'Zong'))

T = TypeVar("T")


# 泛型：TypeVar
def foo(*args: T, **kwargs: T) -> None:
    print(args, kwargs)


foo('a', 'b', x=42, y='c')  # 未见类型不匹配提示

V = Union[str, bytes]


def concat(s1: V, s2: V) -> V:
    return s1 + s2


concat("hello", "world")
concat(b"hello", b"world")
# Union 多参数可以不同类型
# concat("hello", b"world")  # 无类型提示，运行时异常
# concat(b"hello", "world")  # 无类型提示，运行时异常
# concat(42, 100)  # 提示类型不匹配


S = TypeVar("S", str, bytes)


def concat2(s1: S, s2: S):
    return s1 + s2


concat2("hello", "world")
concat2(b"hello", b"world")


# TypeVar 多参数必须同类型
# concat2("hello", b"world")  # 提示类型不匹配，运行时异常
# concat2(b"hello", "world")  # 提示类型不匹配，运行时异常
# concat2(42, 100)  # 提示类型不匹配


# Optional[int] <=> Union[int, None]
def optional_func(num: Optional[int] = None):
    print('Optional: ', num)


optional_func(42)


# 隐式默认为 Any
def hi_any(name: Any) -> Any:
    print(name)


hi_any('haha')


# 可调用对象（函数、类等）
def cf(fn: Callable[[str], str], s: str) -> str:
    return fn(s)


print(cf(hi, 'Eric'))


# 自引用、前置引用
class Tree(object):
    def __init__(self, left: "Tree" = None, right: "Tree" = None):
        self.left = left
        self.right = right


tree = Tree(Tree(), Tree())


# 鸭子类型
# 继承 Protocol 声明接口类型
class Interface(Protocol):
    def close(self) -> None:
        ...


# 不需要实现接口，只需要实现接口所有方法
# class Stream(Interface):
class Stream:
    def close(self) -> None:
        ...


def close_resource(r: Interface) -> None:
    r.close()


s: Stream = Stream()
close_resource(s)
# close_resource("s")


# 注释类型
long_str = "long long string"  # type: str

# 在 .pyi 文件中使用
# 存根文件（stub files）/类型提示文件（type hint files）
