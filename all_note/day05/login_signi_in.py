import getpass
user = {}  ###保存用户名和密码的地方 实际上需要链接数据库
def login():
    username = input('login_username:').strip()
    passwd = getpass.getpass('passwd').strip()
    if user.get(username) != passwd:
        print('\033[31;1mlogin filed\033[0m')
    else:
        print('\33[32;1mlogin success\033[0m')
def sign():
    username = input('login_username:').strip()
    if username == '':
        print('username must be not null')
    elif not username.isalnum():
        print('username_must be num and apl')
    elif username in user:
        print('user exists')
    else:
        passwd = input('passwd:')
        user[username] = passwd

def show_menu():
    cmds = {'0': login, '1': sign}

    text = ''''
    0 login
    1 sign
    2 exit
    '''
    while True:
        choise = input(text).strip()

        if  choise not in ['0','1','2']:
            print('输入正确的 选项')
            continue
        if choise == '2':
            print('exit')
            break
        cmds[choise]()
if __name__ == '__main__':
    show_menu()