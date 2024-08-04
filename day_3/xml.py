import requests
import xml.etree.ElementTree as ET
import io
import datetime as dt

d = dt.date.today()
d_str = d.strftime('%d/%m/%Y')

url = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/01/2024&date_req2=03/08/2024&VAL_NM_RQ=R01235'
# url2 = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=03/08/2024'
url2 = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + d_str
# cbr_xml_text = requests.get(url).text
cbr_xml_text2 = requests.get(url2).text
# fake_file = io.StringIO(cbr_xml_text2)  #фальшивый файл с  методами файла
# content = requests.get(url2).content.decode('cp1251')
# print(cbr_xml_text)
cbr_xml_obj = ET.fromstring(cbr_xml_text2)
# xml_data = ET.parse(fake_file)
# print(xml_data)
# for record in cbr_xml_obj:
#     print(record.attrib['ID'])
#     print(record.find('Value').text) #тег с именем Value
#     for r2 in record:
#         print(r2.tag, r2.text)
f = open('cbr.csv', 'w')
f.write('Код;цена\n')
for v in cbr_xml_obj:
    code = v.find('CharCode').text
    value = float(v.find('Value').text.replace(',', '.'))
    nominal = int(v.find('Nominal').text)
    line = code + ';' + str(round(value/nominal, 10)) + '\n'
    f.write(line)
f.close()

