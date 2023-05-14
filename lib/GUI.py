import time
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from threndClass import PatchMission
from tkinter import messagebox

counter = 1
missionCounter = 1.1


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("搜索引擎图片爬取")
        self.window.geometry("650x400")
        self.window.configure(bg='#C0C0C0')
        global counter
        self.newButton = tk.Button(self.window,
                                   text="新爬虫任务",
                                   command=lambda: self.openNewThrend(),
                                   relief=tk.RAISED,
                                   width=8,
                                   height=1
                                   )
        self.clear = tk.Button(self.window,
                               text="清空任务记录",
                               width=10,
                               height=1,
                               command=lambda: self.clearHistory())
        self.display = tk.Text(self.window,
                               width=70,
                               height=20,
                               )
        self.newButton2 = tk.Button(self.window,
                                    text="图片查找",
                                    width=10,
                                    height=1)
        self.display.configure(bg='#D3D3D3')

    def format(self):
        self.newButton.grid(row=1, column=1, padx=6, pady=6)
        self.newButton2.grid(row=1, column=2, padx=6, pady=6)
        self.clear.grid(row=1, column=3, padx=6, pady=6, columnspan=2)
        self.display.grid(row=2, column=1, columnspan=4, pady=6, padx=40)
        self.window.resizable(0, 0)

    def clearHistory(self):
        self.display.delete(1.1, "end")

    def openNewThrend(self):
        global counter
        temp = ThrendingWindow()
        temp.format()


def addContentToMain(idx, val, target):
    target.insert(idx, val)


class ThrendingWindow:
    def __init__(self):
        global counter
        self.window = tk.Toplevel()
        self.engine = tk.StringVar()
        self.kw = tk.StringVar()
        self.page_num = tk.IntVar()
        self.directory = tk.StringVar()
        self.quantity = 30 if self.engine == "baidu" else 35
        self.header_no = tk.StringVar()
        self.name = tk.StringVar()
        self.window.configure(bg='#C0C0C0')
        global counter
        self.window.title(f"未定进程{counter}")
        self.window.geometry("800x450")

        self.label1 = tk.Label(self.window, text="存储文件路径:")
        self.label2 = tk.Label(self.window, text="关键词")
        self.label3 = tk.Label(self.window, text=f'页数({self.quantity}张/页)')
        self.label4 = tk.Label(self.window, text='搜索引擎')
        self.label5 = tk.Label(self.window, text='浏览器')
        self.label6 = tk.Label(self.window, text="任务名称")

        self.label1.configure(bg='#C0C0C0')
        self.label2.configure(bg='#C0C0C0')
        self.label3.configure(bg='#C0C0C0')
        self.label4.configure(bg='#C0C0C0')
        self.label5.configure(bg='#C0C0C0')
        self.label6.configure(bg='#C0C0C0')
        self.dirText = tk.Entry(self.window,
                                show=None,
                                width=50,
                                state='disabled',
                                textvariable=self.directory)

        self.dirButton = tk.Button(self.window,
                                   text="打开文件夹",
                                   relief=tk.RAISED,
                                   width=10,
                                   height=1,
                                   command=lambda: self.selectPath())
        self.kwText = tk.Entry(self.window, show=None, width=35)

        self.pgText = tk.Entry(self.window, show=None, width=35)

        self.engComb = ttk.Combobox(self.window)

        self.engComb['values'] = ('baidu', 'bing')
        self.engComb.current(0)

        self.headerComb = ttk.Combobox(self.window)
        self.headerComb['values'] = ('google', 'edge', 'fake')
        self.engComb.current(0)

        self.threndName = tk.Entry(self.window, show=None, width=35)
        self.runButton = tk.Button(self.window,
                                   text='开始',
                                   relief=tk.RAISED,
                                   command=lambda: self.beginThrend()
                                   )

        # 和确认按钮绑定在同一事件内以防获取空值

    def getContent(self):
        self.kw = self.kwText.get()
        self.page_num = self.pgText.get()
        self.engine = self.engComb.get()
        self.header_no = self.headerComb.get()
        self.name = self.threndName.get()
        self.directory = self.dirText.get()

    def format(self):
        self.label1.grid(row=1, column=1, padx=10, pady=10)
        self.label2.grid(row=2, column=1, padx=10, pady=10)
        self.label3.grid(row=2, column=3, padx=10, pady=10)
        self.label4.grid(row=3, column=1, padx=10, pady=10)
        self.label5.grid(row=3, column=3, padx=10, pady=10)
        self.label6.grid(row=4, column=1, padx=10, pady=10)

        self.dirButton.grid(row=1, column=4, padx=10, pady=10)
        self.runButton.grid(row=4, column=4, padx=10, pady=10)

        self.dirText.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        self.kwText.grid(row=2, column=2, padx=10, pady=10)
        self.pgText.grid(row=2, column=4, padx=10, pady=10)
        self.threndName.grid(row=4, column=2, padx=10, pady=10)

        self.engComb.grid(row=3, column=2, padx=10, pady=10)
        self.headerComb.grid(row=3, column=4, padx=10, pady=10)

        self.window.columnconfigure(1, weight=2)
        self.window.columnconfigure(2, weight=3)
        self.window.columnconfigure(3, weight=2)
        self.window.columnconfigure(4, weight=2)

        self.window.resizable(0, 0)

    def selectPath(self):
        filepath = askdirectory()
        self.directory.set(filepath)

    def ensureInfo(self):
        global counter
        if not self.directory:
            messagebox.showwarning("警告", "请选择存储路径")
        elif not self.header_no:
            messagebox.showwarning("警告", "请输入浏览器")
        elif not self.page_num:
            messagebox.showwarning("警告", "请输入爬取页数")
        elif not self.kw:
            messagebox.showwarning("警告", "请输入检索关键词")
        if not self.name:
            self.name = f"未命名进程{counter}"

    # def test(self):
    #     self.getContent()
    #     self.ensureInfo()
    #     inputLimitInt(self.pgText)
    #
    #     print(f"{self.kw}\t{self.page_num}\n{self.header_no}\t{self.engine}\n{self.directory}")

    def beginThrend(self):
        global missionCounter
        self.getContent()
        self.ensureInfo()
        root.display.insert(str(round(missionCounter, 1)),
                            f"---开始爬虫任务: {self.name} 时间: {time.ctime()}---\n")
        if inputLimitInt(self.pgText):
            missionCounter += 1
            t = PatchMission(kw=self.kw,
                             page_num=self.page_num,
                             directory=self.directory,
                             header_no=self.header_no,
                             name=self.name
                             )
            self.window.destroy()
            t.run()

            missionCounter += 1

            root.display.insert(str(round(missionCounter, 1)),
                                f"---结束爬虫任务: {self.name} 时间: {time.ctime()}---\n")
            # self.display.insert(missionCounter,
            #                     f"---结束进程: {self.name} 时间: {time.ctime()}")
            # missionCounter += 1
        else:
            self.beginThrend()


def inputLimitInt(target):
    try:
        float(target.get())
        return True
    except:
        messagebox.showwarning("警告", "页数只能输入数字!")
        return False


root = MainWindow()
root.format()
tk.mainloop()
