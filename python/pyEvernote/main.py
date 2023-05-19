# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.constants as constants


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    # print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    host = "sandbox.yinxiang.com"
    consumer_key = "babailong"
    consumer_secret = "e6ca846d76d75a79"
    dev_token = "S=s1:U=50a:E=18261d45f3d:C=1823dc7da60:P=1cd:A=en-devtoken:V=2:H=f55e82b13b3a4535f21b5c951a47a39a"
    client = EvernoteClient(token=dev_token,
                            service_host=host)
    # consumer_key=consumer_key, consumer_secret=consumer_secret,
    # sandbox=True, china=True,
    userStore = client.get_user_store()

    version_ok = userStore.checkVersion(
        "Evernote EDAMTest (Python)",
        constants.EDAM_VERSION_MAJOR,
        constants.EDAM_VERSION_MINOR
    )
    print(version_ok)

    user = userStore.getUser()
    print(user.username)

    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    print("Found ", len(notebooks), " notebooks:")
    for notebook in notebooks:
        print("  * ", notebook.name)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print('PyCharm')
    print('wait...')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
