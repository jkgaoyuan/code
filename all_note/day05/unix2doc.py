####将linux中的换行符\n 替换为 window中的 \r\n,使得文件可以在window中正常查看,
## 该软件在yum 中 提供了名字也叫unix2doc
##也提供了doc2unix的软件
import sys
data = []
da1 = []
def transfer(sfile,deflie):
    with open(sfile) as f1:
        for line in f1:
            blist = list(line)
            blist[-1] = '\r\n'
            f2 = ''.join(blist)
            print(f2)
            data.append(f2)
            print(data)
            f2 = ''.join(data)

            with open(deflie,'w') as f3:

                    f3.write(''.join(f2))  ###将list 转化为 str

transfer(sys.argv[1],sys.argv[2])
