import time


def log(fn):
    def wrapper(*args, **kw):
        print('%s executed' % fn.__name__)
        return fn(*args, **kw)

    return wrapper


def pp(x, y):
    print(x, y)


@log
def add(x, y):
    return x + y


@log
def minus(x, y):
    return x - y


pp = log(pp)
pp('重新为函数', '赋值')


f = add(1, 2)
s = minus(3, 2)
if f != 3:
    print('测试失败!')
elif s != 1:
    print('测试失败!')
