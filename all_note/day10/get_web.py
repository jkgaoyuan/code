import wget
import os
import re
from urllib import request, error

def download(url, fname):
    html = request.urlopen(url)
    with open(fname , 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data: ###当data 为空时
                break
            fobj.write(data)
if __name__ == '__main__':
    ###创建存储图片目录
    download_dir = '/tmp/163'
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    #下载网易首页
    url163 = 'http://www.163.com'
    fname163 = '/tmp/163/163.html'
    if not os.path.exists(fname163):
        download(url163, fname163)
    ###在网页中取出图片url
    img_list = []
    img_patt = '(http|https):[-./\w]+\.(jpg|gpeg|png|gif)'
    cpatt = re.compile(img_patt)
    ###正则匹配
    with open(fname163, encoding='gbk') as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                img_list.append(m.group())
    ## 下载图片

    for img_url in img_list:
        try:
            wget.download(img_url, download_dir)
        except error.HTTPError:
            pass