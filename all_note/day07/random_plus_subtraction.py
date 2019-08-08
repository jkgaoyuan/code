import random
def calculate():

    a = random.randint(0,101)
    b = random.randint(0,101)
    if a < b:
        a ,b = b, a
    c = random.choice('+-')   ## 随机加减法
    if c == '+':
        result = a + b
    else:
        result = a - b
    print('%s %s %s = ?' % (a, c , b))  ###显示计算的公式
    loopnum = 0                         ### 循环次数
    while loopnum < 3:
        try:

            uans = int(input('YOUER ANSWES:'))   ####用户输入答案
        except:
            print()
            continue
        if uans == result:
            print('yes')
            break
        print('no')
        loopnum += 1
    else:
        print('ans is %s' % result)


def main():

    while True:
        calculate()
        try:
            choise = input('continue: Y/N ').strip()[0]
        except IndexError:     ###回车 表示yes
            choise = 'y'
        except (KeyboardInterrupt, EOFError):  ###ctrl + c/d 表示取消
            choise = 'n'

        if choise in 'nN':
            print('baby')
            break

if __name__ == '__main__':
    main()
