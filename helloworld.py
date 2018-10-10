print('你好我是jkgao')

count = 0
while (count<9):
    print('The count is:', count)
    count = count + 1
print('END')
numbers = [12, 37, 65, 100, 77, 53]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0) :
        even.append(number)
        print('even=', even)
    else:
        odd.append(number)
        print('odd=', odd)

