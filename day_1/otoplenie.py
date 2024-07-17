import openpyxl
def c_to_f(c):
    return (c * 9/5) + 32

f = open(r"d:\курсы\курсы Специалист\Python\[Специалист] Python для бизнес - аналитики (2021)\Code\Датасеты\Отопление.txt", 'r')
lines = f.readlines()[14:44]
for line in lines:
    t1 = float(line[51:56])
    t2 = float(line[57:62])
    t1_f = round(c_to_f(t1), 2)
    t2_f = round(c_to_f(t2), 2)


