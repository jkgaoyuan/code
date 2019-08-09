class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp
    def show_me(self):
        print('我是%s, 我的武器是%s' % (self.name, self.weapon))

# class Weapon:
#     def __init__(self, nm, strength):
#         self.wname = nm
#         self.stength = strength
class Warrior(GameRole):
    def __init__(self, nm , weapon,gender):
        GameRole.__init__(self, nm, weapon)
        self.gender = gender
    def attack(self, comment):
        print(comment)
class Mage(GameRole):
    def attack(self, comment):
        print(comment)

if __name__ == '__main__':

    lyn = Mage('李云龙','你他娘的意大利炮呢')
    lyn.show_me()

    bng = Warrior('波澜哥', '让我掀起波澜', '男')
    bng.show_me()
    print(bng.name,bng.gender)
    lyn.attack('李永乐')
    bng.attack('张宇')