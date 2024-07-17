f = open(r"D:\курсы\курсы Специалист\Python\[Специалист] Python для бизнес - аналитики (2021)\Code\Занятие 1\Книга1.csv", 'r')
lines = f.readlines()
# print(lines)
# print(lines[-1].split(';')[-1])
line = lines[-1].split(';')
f = float(line[2].replace(',','.'))
# print(f)

#выгрузка данных в csv
f1 = open('data.csv', 'w')
f1.write('a;b\n')
a = [12, 22, 11, 55, 232, 222, 6544]
b = [12, 3.14, 11, 55, -1, 222, 0]
for ai, bi in zip(a, b):
    # print(ai, bi)
    s = str(ai) + ';' + str(bi).replace('.',',') + '\n'
    # s = f'{ai},{bi}\n'
    f1.write(s)
f1.close() #чтобы файл записался

