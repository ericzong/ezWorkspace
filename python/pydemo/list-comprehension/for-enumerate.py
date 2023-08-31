"""
适用场景：遍历同时需要处理索引和元素
"""
array = ['I', 'love', 'Python']
for i, element in enumerate(array):
    array[i] = '%d: %s' % (i, array[i])
print(array)
