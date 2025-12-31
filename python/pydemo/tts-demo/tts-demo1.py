import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')  # 获取所有可用声音
for i, voice in enumerate(voices):
    print(f"声音 {i} : {voice.name}")
# 选择不同的声音
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')  # 获取当前语速
print(f"当前语速: {rate}")
engine.setProperty('rate', 150)  # 设置语速，默认200，降低一点

volume = engine.getProperty('volume')  # 获取当前音量
print(f"当前音量: {volume}")
engine.setProperty('volume', 0.5)  # 设置音量（范围0.0-1.0）

# 让它说点什么
engine.say("Hello, 这是一段Python代码让电脑开口说话的测试！")
engine.runAndWait()  # 运行

engine.save_to_file("你好，这是一个 Python 生成的语音文件！", "output.mp3")
print("语音文件保存成功！")
