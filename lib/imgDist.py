import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from aip import AipImageClassify


class PicDist:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("进行图片逆向查找")
        self.window.geometry("600x100")
        self.directory = tk.StringVar()
        self.button1 = tk.Button(self.window,
                                 text="选择图片",
                                 width=10,
                                 height=1,
                                 command=lambda: self.selectPath())
        self.button2 = tk.Button(self.window,
                                 text="开始检索",
                                 )
        self.dirText = tk.Entry(self.window,
                                show=None,
                                width=50,
                                state='disabled',
                                textvariable=self.directory)

    def format(self):
        self.button1.grid(row=1, column=1, padx=6, pady=6)
        self.dirText.grid(row=1, column=2, pady=6, padx=6)
        self.button2.grid(row=1, column=3, padx=6, pady=6)

    def selectPath(self):
        filepath = askopenfilename()
        self.directory.set(filepath)


# def findPic(picDir):
#     APP_ID = "27167879"
#     APP_KEY = "fKTF23whPm5nNlaxduecgGlq"
#     SECRET_KEY = "zRjis5Yu2SY8d4A39cB4vGzyShAOtn26"
#
#     client = AipImageClassify(APP_ID, APP_KEY, SECRET_KEY)
#     img = f"{picDir}"
#
#     result = list(client.advancedGeneral(img))
#     t_result = []
#     for i in range(len(result)):
#         temp = (result[i]["score"], result[i])
#         t_result.append(temp)
#     t_result = t_result.sort()
#     f = t_result[0]
#     return f[0], f[1]["keyword"]


t = PicDist()
t.format()
tk.mainloop()
