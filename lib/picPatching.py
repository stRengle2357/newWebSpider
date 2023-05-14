import requests
import param
import re
import os

counter = 600
# import time
# from lxml import etree
from threading import Lock

lock = Lock()

# 作用: 通过百度搜索引擎爬取图片
# 输入: 关键词, 页数, 图片保存路径,  UserAgent编号
# 输出: 无返回值, 直接保存图片
def baiduPicPatching(name, kw, page_num, directory, header_no='google'):
    page_num = int(page_num)
    header = param.defHeader(header_no)
    requestList = []
    url = 'https://image.baidu.com/search/acjson?'
    global counter
    for pn in range(0, 30 * page_num, 30):

        baidu_param = {'tn': 'resultjson_com',
                       # 'logid': '10676375421542742461',
                       'ipn': 'rj',
                       'ct': 201326592,
                       'is': '',
                       'fp': 'result',
                       'fr': '',
                       'word': kw,
                       'queryWord': kw,
                       'cl': 2,
                       'lm': -1,
                       'ie': 'utf-8',
                       'oe': 'utf-8',
                       'adpicid': '',
                       'st': -1,
                       'z': '',
                       'ic': 0,
                       'hd': '',
                       'latest': '',
                       'copyright': '',
                       's': '',
                       'se': '',
                       'tab': '',
                       'width': '',
                       'height': '',
                       'face': 0,
                       'istype': 2,
                       'qc': '',
                       'nc': '1',
                       'expermode': '',
                       'nojc': '',
                       'isAsync': '',
                       'pn': pn,
                       'rn': '30',
                       'gsm': '5a',
                       '1660204617706': ''
                       }
        response = requests.get(url=url, headers=header, params=baidu_param)
        response.encoding = 'utf-8'

        html = response.text
        img_url_list = re.findall('"thumbURL":"(.*?)",', html, re.S)
        print(img_url_list)
        requestList.append(img_url_list)
        if not os.path.exists(directory):
            os.makedirs(directory)

        for imgUrl in img_url_list:
            lock.acquire()
            imgData = requests.get(url=imgUrl, headers=header).content
            with open(os.path.join(directory, f"{counter:08d}.jpeg"), 'wb') as fp:
                fp.write(imgData)
            lock.release()
            counter += 1
    #     requestList.append(img_url_list)
    #     q = []
    #     for i in requestList:
    #         thread = SimpleThrend(f"{name}--{counter}", i, directory, header)
    #         thread.run()
    #         q.append(thread)
    #     for thread in q:
    #         thread.join()
    # print("结束进程")
    # return requestList, kw, baidu_param, directory, header_no


def patching(requestList, header, directory, pn):
    global counter
    if not os.path.exists(directory):
        os.makedirs(directory)
    for tempList in requestList:
        for picUrl in tempList:
            img_data = requests.get(url=picUrl, headers=header).content
            with open(os.path.join(directory, f'{counter:06d}')) as fp:
                fp.write(img_data)
            counter += 1
        # print(f"---第{pn}页内容爬取完毕---")


def pagePatching(UrlList, header, directory, pn):
    global counter
    if not os.path.exists(directory):
        os.makedirs(directory)
    for picUrl in UrlList:
        img_data = requests.get(url=picUrl, headers=header).content
        with open(os.path.join(directory, f'{counter:06d}.jpg')) as fp:
            fp.write(img_data)
        counter += 1
    # print(f"---第{pn}页内容爬取完毕---")


# def bingPicPatching(kw, page_num, directory, header_no='google'):
#     header = param.defHeader(header_no)


