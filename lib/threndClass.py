from time import ctime
from picPatching import baiduPicPatching
import threading
import os
import requests

from threading import Lock
# from picPatching import baiduPicPatching
from queue import Queue

lock = Lock()


# 进程类
# 参数: 进程名称, 关键词(此处和之后同图片爬取函数的参数), 页数, 存储路径, Useragent种类, 是否检测文件夹为空
# 作用: 新建爬虫任务
class PatchMission(threading.Thread):
    def __init__(self, kw, page_num, directory, header_no='google', name=None):
        threading.Thread.__init__(self)
        self.name = name
        self.kw = kw
        self.page_num = page_num
        self.directory = directory
        self.header_no = header_no

    def run(self):
        baiduPicPatching(self.name,
                         self.kw,
                         self.page_num,
                         self.directory,
                         header_no=self.header_no,
                         )


class SimpleThrend:
    def __init__(self, name, targetList, directory, header):
        threading.Thread.__init__(self)
        self.name = name
        self.targetList = targetList
        self.directory = directory
        self.header = header

    def run(self):
        patch(self.targetList, self.directory, self.header)


# return requestList, kw, baidu_param, directory, header_no

def patch(target, directory, header):
    dimCounter = 1
    counter = 1
    for imgUrl in target:
        imgData = requests.get(url=imgUrl, headers=header)
        with open(os.path.join(directory, f"{dimCounter}-{counter:08d}.jpg"), 'wb') as fp:
            fp.write(imgData)
            counter += 1
        dimCounter += 1

# def patchSpeedUp(t_num, targetList):
#     q = []
#     for i in targetList:
#         q.append(i)
#     for j in range(len(q)):
#         thread = SimpleThrend(f"Thrend{str(j)+1}", q[j])
