array = ['I', 'love', 'Python']


def getitem(index, element):
    return '%d: %s' % (index, element)


arrayIndex = [getitem(index, element) for index, element in enumerate(array)]
print(arrayIndex)
