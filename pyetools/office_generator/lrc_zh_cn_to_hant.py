import os
import re
import sys

import pinyin_jyutping
from opencc import OpenCC


class ZhHantGenerator:
    """
    描述：文本文件，简繁转换
    """

    def __init__(self):
        self.trans = ZhHantTransliterator()
        self.pattern = r'([\u4e00-\u9fff]+|[^\u4e00-\u9fff]+)'  # 匹配汉字和非汉字字符

    def __split(self, jyutping: str) -> list[str]:
        return re.findall(self.pattern, jyutping)

    @staticmethod
    def __is_chinese(char: str) -> bool:
        return '\u4e00' <= char[0] <= '\u9fff'

    def process_file(self, lrc_path: str, delimiter: str = ' '):
        with (open(lrc_path, 'r', encoding='utf-8') as src,
              open(lrc_path + '.zh-hant', 'w', encoding='utf-8') as dst):
            lines = src.readlines()

            for line in lines:
                # 移除行尾换行符
                # line = line.rstrip('\n')
                fragments = self.__split(line)

                for fragment in fragments:
                    if self.__is_chinese(fragment):
                        hk_chinese, jyutping = self.trans.transliterate(fragment)
                        for base, rt in zip(hk_chinese, jyutping.split(' ')):  # 粤拼是用空格分隔的
                            dst.write(base)
                    else:
                        dst.write(fragment)

                # dst.write(os.linesep)


class ZhHantTransliterator:
    def __init__(self):
        # 创建一个简体中文到繁体中文的转换器
        self.cc = OpenCC('s2hk')
        self.j = pinyin_jyutping.PinyinJyutping()

    def transliterate(self, lrc: str) -> tuple[str, str]:
        hk_chinese = self.cc.convert(lrc)
        jyutping = self.j.jyutping(hk_chinese, tone_numbers=True, spaces=True)
        return hk_chinese, jyutping


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]
        if len(sys.argv) == 3:
            my_delimiter = sys.argv[2]
            ZhHantGenerator().process_file(file_path, my_delimiter)
        else:
            ZhHantGenerator().process_file(file_path)
    else:
        print("请输入要处理的粤语歌词LRC文件路径：")
        file_path = input()
        print("请输入分割符（可选，直接回车使用默认无分割符）：")
        my_delimiter = input()
        if my_delimiter:
            ZhHantGenerator().process_file(file_path, my_delimiter)
        else:
            ZhHantGenerator().process_file(file_path, '')
