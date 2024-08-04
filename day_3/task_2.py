import json
import datetime as dt
import dateutil

f = open(r'Погода.json', 'r', encoding='utf8')
f2 = open('meteo1.csv', 'w')
f2.write('дата;t_avg;t_min;t_max\n')

data_out_python = []

meteo_dict = json.load(f)
# print(meteo_dict)
for record in meteo_dict['data'][:-1]:
    d_str_iso = record['date']
    t_avg = record['tavg']
    t_min = record['tmin']
    t_max = record['tmax']

    # d_datetime = dt.date.fromisoformat(d_str_iso)
    d_datetime = dateutil.parser.parse(d_str_iso)
    d_str_ddmmyyyy = d_datetime.strftime('%d.%m.%Y')

    #for csv
    line = f'{d_str_ddmmyyyy};{str(t_avg).replace(".", ",")};{t_min};{t_max}\n'
    f2.write(line)

    #for json
    record_out = {
        'date': d_str_ddmmyyyy,
        't_avg': t_avg,
        't_min': t_min,
        't_max': t_max
    }
    data_out_python.append(record_out)

f2.close()
f3 = open('meteo_json_out.json', 'w')
json.dump(data_out_python, f3)
f3.close()

