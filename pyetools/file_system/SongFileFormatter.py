import os
import re
import sys


class SongFileFormatter:
    """
    这个类用于格式化音乐文件的文件名。它可以处理指定目录下的音乐文件，
    将文件名格式化为统一的样式，例如 "歌手名 - 歌曲名"。

    属性:
        extensions (tuple): 会处理的文件类型，包括歌曲和歌词文件。
        deal_with_re (str): 匹配要处理的文件名正则表达式。

    方法:
        __init__(self, root_dir=None): 初始化类实例，设置根目录。
        get_dir(self): 获取用户输入的根目录路径。
        list_files(self): 列出根目录下的所有文件。
        get_trans_filename(self): 获取需要转换的文件名列表。
        deal_with(self): 处理文件名格式化，并打印处理结果。
    """
    extensions = ('.lrc', '.mp3', '.wav', '.flac', '.ape', '.wma',)  # 会处理的文件类型，歌曲或歌词
    deal_with_re = r'(.*?)(\s*-\s*)(.*?)'  # 匹配要处理的文件名正则

    def __init__(self, root_dir=None):
        """
        参数:
            root_dir (str): 要处理的文件夹路径。如果未提供，则会在运行时提示用户输入。
        """
        self.root_dir = root_dir

        self.songs = list()
        self.trans_dict = dict()  # 需格式化
        self.unknown_list = list()  # 无法格式化
        self.formatted_list = list()  # 已格式化
        self.skip_list = list()  # 不处理

        self.get_dir()
        self.list_files()

    def get_dir(self):
        """
        获取用户输入的根目录路径。如果输入的路径不是一个有效的目录，则会提示用户重新输入。
        """
        if not self.root_dir:
            print("请指定处理文件夹路径：")
            while not os.path.isdir(root_dir := input()):
                print("非法文件夹路径，请重新指定：")
            else:
                self.root_dir = root_dir

    def list_files(self):
        """
        遍历目录下的所有文件和子目录，并将文件名添加到 songs 列表中。
        """
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                self.songs.append(file)

    def get_trans_filename(self):
        """
        获取需要转换的文件名列表，并将其存储在 trans_dict 中。
        同时，将已格式化的文件名添加到 formatted_list 中，将无法格式化的文件名添加到 unknown_list 中，
        将不需要处理的文件名添加到 skip_list 中。
        """
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

    def deal_with(self):
        """
        处理文件名格式化，并打印处理结果。
        它会重命名文件，并将重命名后的文件移动到一个名为 "rename" 的子目录中。
        """
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
