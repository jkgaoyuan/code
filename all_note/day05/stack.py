#############
stack = []
def push_it():
    alist = input('输入入栈内容:').strip()
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
  prompt='''
    0 入栈
    1 出栈
    2 查询
    3 退出
    请输入 0 1 2 3
    '''
  while True:
      choice = input(prompt).strip()
      if choice not in ['0', '1', '2', '3']:
          print('TYPE_ERRO TRY AGIN')
          continue

      if choice == '0':
          push_it()
      elif choice == '1':
          pop_it()
      elif choice == '2':
          view_it()
      else:
          print('baby')
          break

if __name__ == '__main__':
    show_menu()





