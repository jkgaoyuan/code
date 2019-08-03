from random import choice
from string import ascii_letters,digits
all_chs = ascii_letters + digits         ###数字 digits  大写字母+小写字母 ascii_letters
def rendpass(n=8):
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch
    return result
if __name__ == '__main__':
    print(rendpass())