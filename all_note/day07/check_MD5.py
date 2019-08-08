import hashlib
import sys
def check (fname):
    m1 = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            date = fobj.read(4096)
            if not date:
                break
            m1.update(date)
        return m1.hexdigest()

if __name__ == '__main__':

    print(check(sys.argv[1]))
