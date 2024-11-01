import xml.etree.ElementTree as ET
from pathlib import Path


def count_leaf_nodes(node):
    """
    递归函数用来计算给定节点下的叶子节点数。
    :param node: ElementTree 的 Element 对象
    :return: 叶子节点的数量
    """
    # 初始化计数器
    leaf_count = 0

    # 检查当前节点是否是叶子节点
    if len(node) == 0:
        return 1

    # 如果不是叶子节点，则递归地检查每个子节点
    for child in node:
        leaf_count += count_leaf_nodes(child)

    return leaf_count


def main(file_path):
    # 解析 FreeMind 文件
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"解析错误: {e}")
        return

    # 计算叶子节点数量
    leaf_count = count_leaf_nodes(root)
    # print(f"叶子节点总数: {leaf_count}")
    return leaf_count


if __name__ == "__main__":
    dir_path = Path('mm')
    for item in dir_path.rglob('*.mm'):
        print(f"{item.name}: {main(item)}")
