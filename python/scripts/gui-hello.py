import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Hello World GUI")

# 在窗口中添加一个标签，显示 "Hello World!"
label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)  # 设置标签的间距

# 运行主循环
root.mainloop()
