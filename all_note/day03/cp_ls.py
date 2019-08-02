##模拟cp 操作 拷贝/bin/ls 到指定位置
# src_fname = '/bin/ls'
# dst_fname = '/tmp/ls'
#
# src_fobj = open(src_fname,'rb')
# dst_fobj = open(dst_fname,'wb')
#
# while 1:
#     data = src_fobj.read(4096) #每次读4096个字节
#     #if len(data) == 0:
#     #if data == b'':
#     if not data: #空为假,判断后的代码不执行 这是判断是否将文件读完
#         break
#     dst_fobj.write(data)
#
# src_fobj.close() #保存文件
# dst_fobj.close() #保存


###形参写法
###在命令行下添加两个参数 在执行
## eg: python3 cp_ls.py /bin/cp /tmp/zhu
import sys
def cp2(src_fname,dst_fname):
    src_fobj = open(src_fname,'rb')
    dst_fobj = open(dst_fname,'wb')
    while 1:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)
    src_fobj.close()
    dst_fobj.close()

cp2(sys.argv[1],sys.argv[2])
