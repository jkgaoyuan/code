# records = [['时间', '收入','花费', '余额', '类型']]
import os
import time
import pickle


def inconme(fname):
    gettime = time.strftime('%Y-%m-%d')
    getmoney = float(input('收入:'))
    getcomment = input('分类:')
    #取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)         ##将读出的fobj 赋值给records
    #计算最新余额
    balance= records[-1][-2] + getmoney     #### 这里的records 相当于一个多远数组 -1 -2 则 分别为 数组的下标 i和j/ i行j列
    #更新列表
    records.append([gettime, getmoney, 0, balance, getcomment])
    #把列表回写到文件
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)
    ###整个文件的跟新思路就是将整个文件都读出来在更新完成后直接覆盖重新完全写入

def spend(fname):
    gettime = time.strftime('%Y-%m-%d')
    getmoney = float(input('消费:'))
    getcomment = input('分类:')
    # 取出所有的记录
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 计算最新余额
    balance = records[-1][-2] - getmoney
    # 更新列表
    records.append([gettime,0 , getmoney, balance, getcomment])
    # 把列表回写到文件

    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def look(fname):
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    # 打印表头'%-12s%-8s%-8s%-10s%-20s'
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'save', 'cost', 'balance','comment') )
    #取出每个记录
    for  record in records:
        # print('%-12s%-8s%-8s%-10s%-20s' % tuple(record))  ###将列表转化为元祖,避免使用list 输出时需要写成list_name[-1]的问题
        print('%-12s%-8s%-8s%-10s%-20s' % (record[0], record[1], record[2], record[3],record[-1]))  ###将列表转化为元祖,避免使用list 输出时需要写成list_name[-1]的问题
def menu():
    fname = 'account.data'
    init_data = [[time.strftime('%Y-%m-%d'), 0, 0, 1000, 'init']]

    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)
    cmds = {'0':inconme, '1':spend, '2':look}

    prompt = '''
    0 收入
    1 花费
    2 查询
    3 退出
    请输入0,1,2,3:
    '''
    while True:
        choise = input(prompt).strip()

        if choise not in ['0', '1', '2', '3']:
            print('text error')
            continue
        if choise == '3':
            print('baby')
            break

        cmds[choise](fname)

if __name__ == '__main__':
    menu()
