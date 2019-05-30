import requests
import datetime
from pytils import dt

f = open('pogoda2.txt', 'w')
i = range(8)
temp = int
tomorrow = datetime.date.today() + datetime.timedelta(1)
#print (tomorrow.strftime('%d-%b-%Y'))
f.write (dt.ru_strftime(u"%d %B",tomorrow, inflected=True))
f.write('\n')
f.write('\n')
tomorrow00 = tomorrow.strftime('%Y-%m-%d 00:00:00')
tomorrow03 = tomorrow.strftime('%Y-%m-%d 03:00:00')
tomorrow12 = tomorrow.strftime('%Y-%m-%d 12:00:00')
tomorrow15 = tomorrow.strftime('%Y-%m-%d 15:00:00')
for case in i:
    if case == 0 :
        city_id= 524305
        f.write('Мурманск')
        f.write('\n')
    if case == 1 :
        city_id= 522260
        f.write('Никель')
        f.write('\n')
    if case == 2 :
        city_id= 525404
        f.write('Мончегорск')
        f.write('\n')
    if case == 3 :
        city_id= 581357
        f.write('Апатиты')
        f.write('\n')
    if case == 4 :
        city_id= 543508
        f.write('Ковдор')
        f.write('\n')
    if case == 5 :
        city_id= 553190
        f.write('Кандалакша')
        f.write('\n')
    if case == 6 :
        city_id= 506762
        f.write('Полярные Зори')
        f.write('\n')
    if case == 7 :
        city_id= 496278
        f.write('Североморск')
        f.write('\n')
    appid = "b8b95704cb2cb597c5b703f02bc7c9f2"  
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list']:
            Date = i['dt_txt']
            if float(i['wind']['speed']) == 0:
                Wind1=str('Штиль')
            else:
                Wind1=float(i['wind']['speed'])
                Wind1=str(Wind1)
                Wind1=Wind1[:3]
                Wind1+=' м/с'# Вывести в переменную скорость ветра
            if Date==tomorrow00 :
                temp = int('{0:+3.0f}'.format(i['main']['temp']))
                f.write('\n')
            if Date==tomorrow03 :
                if temp ==  int('{0:+3.0f}'.format(i['main']['temp'])) :
                    temp = int('{0:+3.0f}'.format(i['main']['temp'])) + 1
                if temp < int('{0:+3.0f}'.format(i['main']['temp'])):
                    if temp > 0:
                        f.write('+',str(temp))
                    else:
                        f.write(str(temp))
                    f.write('\n')
                    f.write( '{0:+3.0f}'.format(i['main']['temp']))
                else:
                    f.write( '{0:+3.0f}'.format(i['main']['temp']))
                    f.write('\n')
                    if temp >0:
                        f.write('+',str(temp))
                    else:
                        f.write(str(temp))
                f.write('\n')
                f.write(i['weather'][0]['description'] )
                f.write('\n')
                f.write(Wind1)
                f.write('\n')
            if Date==tomorrow12 :
                temp = int('{0:+3.0f}'.format(i['main']['temp']))
                f.write('\n')
            if Date==tomorrow15 :
                if temp ==  int('{0:+3.0f}'.format(i['main']['temp'])) :
                    temp = int('{0:+3.0f}'.format(i['main']['temp'])) + 1
                if temp < int('{0:+3.0f}'.format(i['main']['temp'])):
                    f.write(str(temp))
                    f.write('\n')
                    f.write( '{0:+3.0f}'.format(i['main']['temp']))
                else:
                    f.write( '{0:+3.0f}'.format(i['main']['temp']))
                    f.write('\n')
                    f.write(str(temp))
                f.write('\n')
                f.write(i['weather'][0]['description'] )
                f.write('\n')
                f.write(Wind1)
                f.write('\n')
    except Exception as e:
        print("Exception (forecast):", e)
        pass
f.close()
