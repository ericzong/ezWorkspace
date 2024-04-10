class Score:
    """
    描述符类
    """
    def __set__(self, instance, value):
        """
        定义属性赋值行为
        1. 属性值只能设置一次，不可修改
        2. 属性值在 [0, 100] 区间
        :param instance: 属性所在的实例
        :param value: 属性值
        """
        if hasattr(instance, 'value'):
            raise ValueError('分数不可修改')

        if 0 <= value <= 100:
            instance.value = value
        else:
            raise ValueError(f'分数必须在[0,100]区间，现在是{value}')

    def __get__(self, instance, owner):
        """
        定义访问属性行为
        :param instance: 属性所在的实例
        :param owner: 属性所属的类
        """
        return instance.value

    def __delete__(self, instance):
        """
        定义属性删除行为
        不支持删除该属性
        :param instance: 属性所在的实例
        """
        raise Exception('不支持删除属性')


class Student:
    score: int = Score()

    def __init__(self, score: int):
        self.score = score

    def print_score(self):
        print(self.score)


if __name__ == '__main__':
    p1 = Student(60)
    p1.print_score()

    try:
        p1.score = 80
    except Exception as e:
        print(e.args[0])

    try:
        del p1.score
    except Exception as e:
        print(e.args[0])

    try:
        p2 = Student(250)
        p2.print_score()
    except Exception as e:
        print(e.args[0])
