


str1 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
str2 = ' Chrome/103.0.0.0 Safari/537.36'
str3 = ' Edge/103.0.1264.62'
chrome_UA = str1 + str2
EDGE_UA = str1 + str2 + str3
# fake_UA = UserAgent()
chrome_headers = {
    'User-agent': chrome_UA
}
EDGE_headers = {
    'User-agent': EDGE_UA
}
# Fake_headers = {
#     'User-agent': fake_UA
# }


# 作用: 获取爬虫的header
# 输入: google, edge, 或者fake三者其一
# 输出: 浏览器或者伪造的UserAgent, 默认为chrome浏览器
def defHeader(header_no):
    if header_no == 'google':
        header = chrome_headers
    elif header_no == 'edge':
        header = EDGE_headers
    # elif header_no == 'fake':
    #     header = Fake_headers
    else:
        header = chrome_headers
    return header

