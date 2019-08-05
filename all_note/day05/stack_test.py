# stack = []
# def inputtext():
#     data = input('data:').strip()
#     if data:
#         stack.append(data)
#     else:
#         print('null ')
#
# def output():
#     if stack:
#         print('stack is %s' % stack)
#     else:
#         print('null')
# def view():
#     print(stack)
# def menu():
#     text = '''
#     0 input
#     1 output
#     2 view
#     3 exit
#     '''
#     while 1:
#         choise = input(text).strip()
#         if choise not in ['0','1','2','3']:
#             print('text erro')
#         elif choise == '0':
#             inputtext()
#         elif choise == '1':
#             output()
#         elif choise == '2':
#             view()
#         elif choise == '3':
#             print('baby')
#             break
#         else:
#             continue
# if __name__ == '__main__':
#     menu()


stack = []

def inputtext():
    data = input().strip()
    if data:
        stack.append(data)
    else:
        print('text is null')
def outout():
    if stack:
        print('stack is %s' % stack)
    else:
        print('null')
def view():
    print(stack)

def menu():
    cmds = {'0':inputtext,'1':outout,'2':view}   ####cmds 是个字典
    text = '''
      0 input
     1 output
     2 view
     3 exit
    '''
    while 1:
        choise = input(text).strip()
        if choise not in ['0','1','2','3']:
            print('text erro')
            continue
        if choise == '3':
            print('baby')
            break
        cmds[choise]()

if __name__ == '__main__':
    menu()