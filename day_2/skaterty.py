import re
import csv

sku_regexp = r"арт\.([0-9А-Яа-я]{2,3}[\-|\.]?[0-9А-Яа-я]{1,6})"   #r - чтобы не было конфликтов из-за \
size_regexp = r"(\d+)[*xхХ]{1}([0-9]+)"

f = open(r'd:\курсы\курсы Специалист\Python\[Специалист] Python для бизнес - аналитики (2021)\Code\Занятие 2\Скатерти1.csv', 'r', encoding='utf8')
f2 = open(r"Скатерти2.csv", 'w', encoding='utf-8')
f2.write('Товар;Количество(масса  нетто);Цена,руб. коп.;Сумма без учета НДС, руб. коп.;сумма,  руб. коп.;Сумма с учетом НДС, руб. коп.;артикул;длина;ширина\n')
new_file_lines = []
# f = open(r'Скатерти.csv', 'r', encoding='utf8')
# f.seek(0) #переместится в начало курсор
data = csv.reader(f, delimiter=';')
for row in data:
    # print(row)
    name = row[0]
    sku_match = re.search(sku_regexp, name)
    if sku_match is not None:
        sku = sku_match.group(1)
    else:
        sku = 'Нет'
    #print(sku)

    dim_match = re.search(size_regexp, name)
    #print(dim_match)
    if dim_match is not None:
        size1 = dim_match.group(1)
        size2 = dim_match.group(2)
        l = max(size1, size2)
        w = min(size1, size2)
    else:
        l = 0
        w = 0

    line = ';'.join(row)
    line += ';' + sku + ';' + str(l) + ';' + str(w) + '\n'
    new_file_lines.append(line)
f2.writelines(new_file_lines)
f2.close()

