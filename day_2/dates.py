import datetime as dt
import dateutil

dates = ['30.04.15', '02.05.15', '01.04.15','01.05.15','29.01.15']
print(sorted(dates))

d1 = dt.date(2021, 1, 1) #y, m, d
d2 = dt.date.today()
print(d1, d2)
print(d1 > d2)
print(d2 - d1)
print(d2 + dt.timedelta(days=100))
print(d2.strftime('%d.%m.%y'))
print(d2.strftime('%d.%m.%Y'))
print(d2.strftime('%d/%m/%y'))
print(d2.strftime('%d hello /%m/%y'))
print(dt.datetime.now())
print(dt.datetime.now().timestamp())

print(dateutil.parser.parse('02.03.2021', dayfirst=True))  #распознаёт по-американски 3 февраля если нет dayfirst
print(dateutil.parser.parse('2021-03-02'))
print(dateutil.parser.parse('3/2/21').date())

