import csv
import sys


def split_yaml_frontmatter(lines):
    """
    将Markdown内容分割为YAML frontmatter部分和主要内容部分。
    返回: (frontmatter_lines, content_lines)
    """
    if not lines:
        return [], []
    # 检查是否以YAML frontmatter标记（---）开头
    if lines[0].strip() == '---':
        # 寻找结束标记
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                # 返回frontmatter（包括起始和结束标记）和剩余内容
                return lines[:i + 1], lines[i + 1:]
        # 未找到结束标记，视为无frontmatter
        return [], lines
    else:
        # 无YAML frontmatter
        return [], lines


def add_ruby_tags(text, mapping):
    """
    根据映射字典为文本中的字词添加<ruby>标签。
    按字词长度降序排序，优先处理长词，避免部分匹配。
    """
    # 按字词长度降序排序键
    sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
    for word in sorted_keys:
        pinyin = mapping[word]
        # 替换所有出现的字词，避免重叠匹配
        text = text.replace(word, f'<ruby>{word}<rt>{pinyin}</rt></ruby>')
    return text


def main(md_file, csv_file, output_file):
    """
    主函数：读取CSV注音数据，处理MD文件，并输出带注音的结果。
    """
    # 读取CSV文件，构建字词到注音的映射
    word_to_pinyin = {}
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                word = row['字词']
                pinyin = row['注音']
                word_to_pinyin[word] = pinyin
    except FileNotFoundError:
        print(f"错误：CSV文件 '{csv_file}' 未找到。")
        sys.exit(1)
    except KeyError as e:
        print(f"错误：CSV文件必须包含 '字词' 和 '注音' 列。缺失列: {e}")
        sys.exit(1)

    # 读取Markdown文件
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"错误：Markdown文件 '{md_file}' 未找到。")
        sys.exit(1)

    # 分割YAML frontmatter和歌词内容
    frontmatter_lines, content_lines = split_yaml_frontmatter(lines)
    content_text = ''.join(content_lines)

    # 为歌词内容添加注音标签
    processed_content = add_ruby_tags(content_text, word_to_pinyin)

    # 写入输出文件（保留frontmatter）
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(frontmatter_lines)  # 写入frontmatter部分
            f.write(processed_content)  # 写入处理后的内容
        print(f"注音完成！结果已保存到: {output_file}")
    except IOError as e:
        print(f"错误：写入输出文件失败 - {e}")
        sys.exit(1)


if __name__ == '__main__':
    # 命令行参数处理
    if len(sys.argv) != 4:
        print("用法: python add_pinyin.py input.md input.csv output.md")
        sys.exit(1)
    input_md = sys.argv[1]
    input_csv = sys.argv[2]
    output_md = sys.argv[3]
    main(input_md, input_csv, output_md)
