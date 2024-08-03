#"[MМ]?(\d+[\.,]?\d+)[*xх]{1}([0-9]+[\.,]?[0-9]+)|[MМ](\d+)\s?[*xх](\d+)|[MМ](\d+)|(\d+)[*xх]{1}([0-9]+)"gm
#"\((\d+[\.,]?\d*)\s[шт\.|кг]{2,3}\)"gm
import re

size_regexp = r'[MМ\(]?(\d+[\.,]?\d*)\)?\s?[*xх]([0-9]+[\.,]?[0-9]*)'
size_nut_regexp = r'[MМ](\d+)'
pcs_regexp = r'\((\d+[\.,]?\d*)\s[шт\.]{2,3}\)'
kgs_regexp = r'\((\d+[\.,]?\d*)\sкг\)'
f = open(r'd:\курсы\курсы Специалист\Python\[Специалист] Python для бизнес - аналитики (2021)\Code\Занятие 2\Болты.csv', 'r', encoding='utf8')
f2 = open(r"Болты2.csv", 'w', encoding='utf-8')
header = f.readline()
header = header.replace('\n', ';diameter;length;weight;pcs\n')
f2.write(header)
lines = f.readlines()
f.close()
for line in lines:
    diameter = ""
    length = ""
    weight = ""
    pcs = ""
    cells = line.split(';')
    name = cells[0]
    cells[4] = 'https://moscow.petrovich.ru' + cells[4]

    m1 = re.search(size_regexp, name)
    if m1 is not None:
        size1 = float(m1.group(1).replace(',', '.'))
        size2 = float(m1.group(2).replace(',', '.'))
        diameter = min(size1, size2)
        length = max(size1, size2)
    else:
        m2 = re.search(size_nut_regexp, name)
        if m2 is not None:
            diameter = m2.group(1)

    m3 = re.search(kgs_regexp, name)
    if m3 is not None:
        weight = m3.group(1)

    m4 = re.search(pcs_regexp, name)
    if m4 is not None:
        pcs = m4.group(1)

    if pcs == "" and weight == "":
        pcs = 1

    #print(diameter, length, weight, pcs)
    cells[-1] = cells[-1].replace('\n', '')
    cells += [str(diameter).replace('.', ','), str(length).replace('.', ','), str(weight).replace('.', ','), str(pcs)]
    line_new = ';'.join(cells) + '\n'
    f2.write(line_new)
f2.close()
