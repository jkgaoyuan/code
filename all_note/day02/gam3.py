import random
pwin = 0
cwin = 0
while 1:  #人机 赢了不够2次 继续执行

    all_list = ['石头','拳头','布']
    win_list = [['石头','拳头'],['石头','布'],['拳头','布']] #前面是用户后面是电脑
    prompt = '''0 石头
    1 拳头
    2 布
    请选择'''
    computer = random.choice(all_list)
    ind = int(input(prompt))
    play = all_list[ind]
    print('play: %s,computer: %s' % (play,computer) )
    if play == computer:

                print('\033[32;1m平局\033[0m')

    elif [play,computer] in win_list:
                print('\033[31;1m赢了\033[0m')
                pwin += 1


    else:
                print('\033[32;1m失败\033[0m')

                cwin += 1

    if pwin == 2 or cwin == 2:
        break
    else:
        continue