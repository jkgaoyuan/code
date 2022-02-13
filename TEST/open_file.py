#open file
# text = input("输入字符串")
text = ['physics', 'chemistry', '1997', '2000']
print(type(text))

text_str = ','.join(text)

fo = open("output.txt","w")

fo.write(text_str)

fo.close()
