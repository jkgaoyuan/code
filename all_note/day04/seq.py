alist = ['bob','alice','tom','jeery']

for i in range(len(alist)):
    print(i,alist[i])

print(list(enumerate(alist)))

for data in enumerate(alist):
    print(data)

for i,name in enumerate(alist):
    print(i,name)