class Context(object):

    def __init__(self):
        print('init...')

    def __enter__(self):
        """
        在 with 语法体执行前执行
        """
        print('enter...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        在 with 语法体执行后执行
        :param exc_type: 异常类型（如有），否则为 None
        :param exc_val: 异常值（如有），否则为 None
        :param exc_tb: 跟踪信息（如有），否则为 None
        :return:
        """
        print('exit...')


ctx = Context()

with ctx:
    print('run...')
