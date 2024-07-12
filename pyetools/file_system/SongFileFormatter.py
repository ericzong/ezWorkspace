import os
import re
import sys


class SongFileFormatter:
    extensions = ('.lrc', '.mp3', '.wav', '.flac', '.ape', '.wma',)  # 会处理的文件类型，歌曲或歌词
    deal_with_re = r'(.*?)(\s*-\s*)(.*?)'  # 匹配要处理的文件名正则
    # formatted_re = r'.+ - .+'  # 已格式化的文件名正则

    def __init__(self, root_dir=None):
        self.root_dir = root_dir

        self.songs = list()
        self.trans_dict = dict()  # 需格式化
        self.unknown_list = list()  # 无法格式化
        self.formatted_list = list()  # 已格式化
        self.skip_list = list()  # 不处理

        self.get_dir()
        self.list_files()

    def get_dir(self):
        if not self.root_dir:
            print("请指定处理文件夹路径：")
            while not os.path.isdir(root_dir := input()):
                print("非法文件夹路径，请重新指定：")
            else:
                self.root_dir = root_dir

    def list_files(self):
        # 遍历目录下的所有文件和子目录
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                self.songs.append(file)

    def get_trans_filename(self):
        for song_filename in self.songs:
            # filename.ext → filename, .ext
            song_name, ext = os.path.splitext(song_filename)
            # 后缀名不是歌曲或歌词，跳过不处理
            if ext not in SongFileFormatter.extensions:
                self.skip_list.append(song_filename)
                continue

            # 文件名中 - 多于一个，将不知道如何处理
            if song_name.count('-') > 1:
                self.unknown_list.append(song_filename)
                continue

            trans_name = re.sub(SongFileFormatter.deal_with_re, r'\1 - \3', song_name)

            if trans_name != song_name:  # 文件名有变化的，则需要格式化
                self.trans_dict[song_filename] = trans_name + ext
            else:
                self.formatted_list.append(song_filename)
                # match = re.fullmatch(SongFileFormatter.formatted_re, song_name)
                # if match is not None:
                #     self.formatted_list.append(song_filename)
                # else:
                #     self.unknown_list.append(song_filename)

    def deal_with(self):
        self.get_trans_filename()
        print("已处理", len(self.trans_dict), self.trans_dict)
        print("无法处理", len(self.unknown_list),self.unknown_list)
        print("无需处理", len(self.formatted_list), self.formatted_list)
        print("不处理", len(self.skip_list), self.skip_list)

        try:
            # root_dir_fd = os.open(self.root_dir, os.O_RDWR)
            rename_path = os.path.join(self.root_dir, 'rename')
            if not os.path.exists(rename_path):
                os.mkdir(rename_path)
            for old, new in self.trans_dict.items():
                os.rename(os.path.join(self.root_dir, old), os.path.join(rename_path, new))
        except PermissionError as e:
            print(f"没有权限访问目录: {e}")
        except OSError as e:
            print(f"重命名失败：{e}")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        instance = SongFileFormatter(sys.argv[1])
    else:
        instance = SongFileFormatter()
    instance.deal_with()
