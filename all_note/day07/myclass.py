### 类
class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp
    def show_me(self):
        print('我是 %s , 武器 %s' %(self.name,self.weapon))
    def speak(self, content):
        print('%s 在此, %s' % (self.name, content))
    def attack(self, dest):
        print('攻击:%s' % dest)

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法
    # 调用通过类创建的方法，实例自动作为第一个参数传递
    lb = GameRole('吕布' ,'方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.speak('人在塔在')
    zf = GameRole('张飞', '啦啦啦')
    print(zf.name, zf.weapon)
    zf.show_me()
    zf.speak('你大爷的')
    zf.attack('曹操')
    lb.attack('曹操')
    lyn = GameRole('李云龙', '三八大盖')
    print(lyn.name, lyn.weapon)
    lyn.show_me()
    lyn.speak('在下三八六旅李云龙')
    lyn.attack('坂田')
