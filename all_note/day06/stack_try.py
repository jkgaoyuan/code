stack = []
def push_it():
    try:
        alist = input('输入入栈内容:').strip()
    except (KeyboardInterrupt, EOFError):
        print()
        return
    if alist:
        stack.append(alist)
    else:
        print('input is null')

def pop_it():
    if stack:
        print('出栈: %s ' % stack.pop())
    else:
        print('null stack')

def view_it():

    print('stack is %s :' % stack )

def show_menu():
    cmds = {'0': push_it,'1': pop_it ,'2' : view_it}   ###使用字典来简化 判断, 将 输入的字符和字典中的key进行匹配来确定执行什么
    prompt='''
        0 入栈
        1 出栈
        2 查询
        3 退出
        请输入 0 1 2 3
        '''
    while  True:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'
        if choice not in ['0','1','2','3']:
            print('TYPE_ERRO TRY AGIN')
            continue

        if choice == '3':
            print('baby')
            break
        cmds[choice]()
if __name__ == '__main__':
    show_menu()
