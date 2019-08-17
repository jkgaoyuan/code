# 使用 Jenkins 实现cidc 功能 ,在本机执行
import os
import requests
import wget
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    # "有新版本返回True，否则返回False"
    # 本地没有版本文件，返回True
    if not os.path.exists(ver_fname):
        return True

    # 取出本地版本文件内容
    with open(ver_fname) as fobj:
        version = fobj.read()

    # 取出远程最新版本号
    r = requests.get(ver_url)

    # 判断版本号一致为False，不一致为True
    if version == r.text:
        return False
    else:
        return True

def check_app(md5_url, fname):
    "校验软件包，未损坏返回True，损坏返回False"
    # 计算本地md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 读取远程md5值
    r = requests.get(md5_url)

    # 判断
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy(app_fname, deploy_dir):
    "部署软件：解压、创建链接"
    # 解压缩
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 创建链接
    dest = '/var/www/html/nsd1903'
    app_dir = os.path.basename(app_fname) # myblog-1.0.tar.gz
    app_dir = app_dir.replace('.tar.gz', '')  # myblog-1.0
    app_dir = os.path.join(deploy_dir, app_dir) # 绝对路径

    # 如果链接已经存在，先删除，否则无法再创建
    if os.path.exists(dest):
        os.remove(dest)

    os.symlink(app_dir, dest)


if __name__ == '__main__':
    # 如果未发现新版本，则退出
    deploy_dir = '/var/www/deploy'          ###项目解压路径, 又该目录 产生软连接到 网站根目录, 版本切换只需要更换软连接就好了
    download_dir = '/var/www/download'      ###将Jenkins项目下载到该目录,wget 错误请确认该,目录是否存在
    ver_url = 'http://192.168.1.50/deploy/live_ver'  ## Jenkins当前使用 库地址
    ver_fname = os.path.join(deploy_dir, 'live_ver')
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载
    r = requests.get(ver_url)
    ver = r.text.strip()   # 取出版本号
    app_url = 'http://192.168.1.50/deploy/pkgs/myblog-%s.tar.gz' % ver  ###Jenkins 项目地址
    wget.download(app_url, download_dir)
    #              下载地址,保存地址

    # 检查软件是否损坏，损坏则删除软件包并退出
    md5_url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not check_app(md5_url, app_fname):
        print('文件已损坏。')
        os.remove(app_fname)
        exit(2)

    # 部署
    deploy(app_fname, deploy_dir)

    # 更新本地live_ver文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)

    wget.download(ver_url, ver_fname)