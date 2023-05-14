import tkinter as tk
import threading


class Window:
    def __init__(self, param1, param2):
        self.param1 = param1
        # 以此为例定义所需的变量

        self.window = tk.Tk()
        # self.window = tk.Toplevel()
        # self.style = style
        # 在此处定义窗口和尺寸等样式

        self.button = tk.Button(self.window, text="")
        # 以此为例定义数个组件

    def format(self):
        self.button.grid(row=1, column=1, pady=6, padx=6)
        # 在format方法中确定在表格结构中的位置

    def function1(self):
        pass
    # 定义数个窗口所需的功能


def findPic(picDir):
    APP_ID = "xxxxxxx"
    # 输入参数
    client = AipImageClassify(APP_ID, APP_KEY, SECRET_KEY)
    # 实例化客户端类
    img = get_file_content(f"{picDir}")

