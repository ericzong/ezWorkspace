import sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.oxml.ns import qn
from docx.shared import Pt
from jamdict import Jamdict
import fugashi

# 初始化 Jamdict 对象
# jam = Jamdict()

# 日语歌词生成器
# 描述：输入一个文本文件生成一个 Word 文档。其中：
#   1. 为每个日本汉字添加平假名注音
class LrcHiraganaGenerator:
    def __init__(self):
        self.trans = JapaneseTransliterator()
        # 创建一个新的 Word 文档
        doc = Document()
        style = doc.styles['Normal']
        font = style.font
        font.name = 'BIZ UDMincho Medium'
        font.size = Pt(12)
        self.doc = doc

    def process_file(self, lrc_path: str):
        with open(lrc_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            paragraph = self.doc.add_paragraph()
            for word in self.trans.tagger(line):
                if word.feature.kana:
                    # 将片假名转换为平假名
                    hiragana = self.trans.katakana_to_hiragana(word.feature.kana)
                    # 如果有汉字，标注平假名
                    if word.surface != hiragana:
                        DocxLrcXmlWriter(paragraph).write_lrc(word.surface, hiragana)
                    else:
                        paragraph.add_run(word.surface)
                else:
                    paragraph.add_run(word.surface)
                    paragraph.add_run(" ")

        self.doc.save(lrc_path + '.ja.docx')

class JapaneseTransliterator:
    def __init__(self):
        self.tagger = fugashi.Tagger()

    def katakana_to_hiragana(self, kana):
        """将片假名转换为平假名"""
        hiragana = ""
        for char in kana:
            if 0x30A0 <= ord(char) <= 0x30FF:  # 检查是否为片假名
                hiragana += chr(ord(char) - 0x60)  # 转换为平假名
            else:
                hiragana += char
        return hiragana

class DocxLrcXmlWriter:
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def write_lrc(self, base: str, rt: str):
        pre_ele = f'''
          <w:r {nsdecls('w')}>
            <w:rPr>
              <w:rFonts w:hint="eastAsia" w:eastAsia="宋体" w:cs="宋体"/>
              <w:sz w:val="28"/>
              <w:szCs w:val="28"/>
              <w:shd w:val="clear" w:color="auto" w:fill="auto"/>
              <w:lang w:eastAsia="ja-JP"/>
            </w:rPr>
            <w:fldChar w:fldCharType="begin"/>
          </w:r>
        '''

        post_ele = f'''
          <w:r {nsdecls('w')}>
            <w:rPr>
              <w:rFonts w:hint="eastAsia" w:eastAsia="宋体" w:cs="宋体"/>
              <w:sz w:val="28"/>
              <w:szCs w:val="28"/>
              <w:shd w:val="clear" w:color="auto" w:fill="auto"/>
              <w:lang w:eastAsia="ja-JP"/>
            </w:rPr>
            <w:fldChar w:fldCharType="end"/>
          </w:r>
        '''

        ruby_xml = r'''
          <w:r {0}>
            <w:rPr>
              <w:rFonts w:hint="eastAsia" w:eastAsia="宋体" w:cs="宋体"/>
              <w:sz w:val="28"/>
              <w:szCs w:val="28"/>
              <w:shd w:val="clear" w:color="auto" w:fill="auto"/>
              <w:lang w:eastAsia="ja-JP"/>
            </w:rPr>
            <w:instrText xml:space="preserve"> EQ \* jc0 \* "Font:微软雅黑" \* hps12 \o \ad(\s \up 15({1}),{2})</w:instrText>
          </w:r>
        '''.format(nsdecls('w'), rt, base)

        self.paragraph._p.append(parse_xml(pre_ele))
        self.paragraph._p.append(parse_xml(ruby_xml))
        self.paragraph._p.append(parse_xml(post_ele))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        print("请输入要处理的日语歌词文件路径：")
        file_path = input()

    LrcHiraganaGenerator().process_file(file_path)