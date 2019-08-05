import sys
# def transfer(sfile,dfile):
def transfer(sfile,deflie):
    with open(sfile) as f1:
        for line in f1:
            blist = list(line)
            blist[-1] = '\r\n'
            print(blist)
            with open(deflie) as f2:
             f2.write(blist)

transfer(sys.argv[1],sys.argv[2])
