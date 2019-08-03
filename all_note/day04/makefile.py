# import os
#
# def get_filename():
#     while 1:
#         file_name = input('输入文件名: ')
#         #os.path.exists(file_name) ==> 判断文件存在否
#         if not os.path.exists(file_name):
#             break
#         print('文件已存在')
#     return file_name
# def get_content():
#     content = []
#     print('请输入内容，输入end结束输入：')
#     while 1:
#         line = input('(end to quit)>')
#         if line == 'end':
#             break
#         # content += line
#         content.append(line + '\n')
#     return content
#
# def wfile(file_name, content):
#     with open(file_name, 'w') as fobj: #### with 打卡文件 with 结束后文件自动关闭
#         fobj.writelines(content)
#
# if __name__ == '__main__':
#     file_name = get_filename()
#     content = get_content()
#     wfile = (file_name, content)

####在命令行执行这个  文件
import os

def get_fname():
    while True:
        fname = input('文件名: ')
        # os.path.exists(fname) => 文件已存在返回True
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []

    print('请输入内容，输入end结束输入：')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line + '\n')

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
