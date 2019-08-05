### 简单的判断用户的登录和注册
import getpass
userdb = {}

def register():
     username = input('username:').strip()
     if username == '':
         print('usersname is null')
     elif not username.isalnum():
         print('only for num and apl ')
     elif username in userdb:
         print('user exits')

     else:
         passwd = input('passwd').strip()
         userdb[username] = passwd

def login():
    username = input('username:').strip()
    passwd = getpass.getpass('passwd').strip()
    if userdb.get(username) != passwd:
        print('login sucess')
    else:
        print('filed')
def menu():
    cmds = {'0':register,'1':login}
    text = '''
    0 register
    1 login
    2 exit 
    text number to choise function
    '''
    while 1:
        choise = input(text).strip()
        if choise not  in ['0','1','2']:
            print('text erro')
            continue
        if choise == '2':
            print('baby')
            break
        cmds[choise]()

if __name__ == '__main__':
    menu()