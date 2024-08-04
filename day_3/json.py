import requests
import datetime as dt
import json

f2 = open('meteo2.csv', 'w')
f2.write('дата;t_avg;t_min;t_max\n')

data_out_python = []

d1 = dt.date.today()
d2 = d1 - dt.timedelta(days=100)
d1_str = d1.strftime('%Y-%m-%d')
d2_str = d2.strftime('%Y-%m-%d')
station = 'KNYC0'

url = "https://meteostat.p.rapidapi.com/stations/meta"
url2 = "https://meteostat.p.rapidapi.com/stations/daily"
# url2 = f"https://meteostat.p.rapidapi.com/stations/daily?station={station}&start={d2_str}&end={d1_str}"

querystring1 = {"id":"10637"}
querystring2 = {"station":"KNYC0", "start": d2_str, "end": d1_str}

headers1 = {
	"x-rapidapi-key": "ba20eb343amsh44adf13c55ad9c2p1498bajsn57dad9beba8b",
	"x-rapidapi-host": "meteostat.p.rapidapi.com"
}

headers = {
	"x-rapidapi-key": "ba20eb343amsh44adf13c55ad9c2p1498bajsn57dad9beba8b",
	"x-rapidapi-host": "meteostat.p.rapidapi.com"
}

response = requests.get(url2, headers=headers, params=querystring2)
# response = requests.get(url2, headers=headers)

# json = response.json()
meteo_text = response.text
# print(json)
meteo_dict = json.loads(meteo_text)

for record in meteo_dict['data']:
    d_str_iso = record['date']
    t_avg = record['tavg']
    t_min = record['tmin']
    t_max = record['tmax']

    d_datetime = dt.date.fromisoformat(d_str_iso)
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
f3 = open('meteo_json_out2.json', 'w')
json.dump(data_out_python, f3)
f3.close()
