class A:
    def func(self):
        print('A func')
    def funcd(self):
        print('in a ')
class B:
    def funcb(self):
        print('b funb')
    def fund(self):
        print('in b')
class C(A,B):
    def funcc(self):
        print('in c')
if __name__ == '__main__':
    c1 = C()
    c1.funca()
    c1.funcb()
    c1.funcc()
    c1.funcd()