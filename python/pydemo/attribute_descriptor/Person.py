class Score:
    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.value = value
        else:
            raise ValueError(f'score must between 0 and 100 but {value}')

    def __get__(self, instance, owner):
        return instance.value

    def __delete__(self, instance):
        raise Exception('del unsupported')


class Person:
    score: int = Score()

    def __init__(self, score: int):
        self.score = score

    def print_score(self):
        print(self.score)


if __name__ == '__main__':
    p1 = Person(60)
    p1.print_score()

    try:
        del p1.score
    except Exception as e:
        print(e.args[0])

    try:
        p2 = Person(250)
        p2.print_score()
    except Exception as e:
        print(e.args[0])
