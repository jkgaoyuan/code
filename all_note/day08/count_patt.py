import  re
def count_patt(fname, patt):
    ressult = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                ressult[key] = ressult.get(key, 0) + 1
    return ressult
if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
    # n = [[count_patt(fname, ip)]]
    # print(n)