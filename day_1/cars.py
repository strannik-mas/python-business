MILES_IN_KM = 0.62
RUB_IN_USD = 73.5

f = open(r'vw.csv', 'r', encoding='utf8')
# f.read(1)   #пропустили 1 служебный символ
f.readline()    #пропускаем 1 строку в никуда - заголовки, каретка на 2 строке
f2 = open('cars_vw.csv', 'w', encoding='utf-8')
f2.write('kmage;miles;priceRUB;priceUSD;vol;power;fuel\n')
lines = f.readlines()
# for line in lines[1:]:      #тут создаётся копия списка
for line in lines:
    row = line.split(';')   #list cells
    # kmage = row[1].replace(' ', '')[:-2]
    if row[1] == 'Новый':
        kmage = miles = 0
    else:
        kmage = int(row[1].replace(' ', '').removesuffix('км'))
        miles = round(kmage * MILES_IN_KM)
    # priceRUB = int(row[3].replace(' ', '').removesuffix('₽').removeprefix('от'))
    priceRUB = int(row[3].replace(' ', '').removesuffix('\u20BD').removeprefix('от'))
    # priceRUB = int("".join(list(filter(str.isdigit, row[3]))))  #isdigit - без скобок, т.к. это указатель на функцию
    priceUSD = round(priceRUB / RUB_IN_USD, 2)
    # engineArr = row[9].split('/')
    # volume = engineArr[0].replace(' ', '').removesuffix('л')
    # power = engineArr[1].replace(' ', '').removesuffix('л.с.')
    vol, power, fuel = row[-1].split('/')
    vol = float(vol.replace(' л', ''))
    power = int(power.replace('л.с.', ''))

    # print(f'Пробег, км: {kmage}; Пробег, мили: {round(miles)}; Цена, руб: {priceRUB}; Цена, USD: {round(priceUSD, 2)}; Объём, л: {vol}; Мощность, л.с.: {power}; Тип топлива: {fuel}')
    s = f'{kmage};{miles};{priceRUB};{priceUSD:10.1f};{vol};{power};{fuel}'.replace('.',',')
    f2.write(s)
f2.close()