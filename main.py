from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import datetime
import time
import sys
pm25=True
write = 0
prev = []
current = []


url = input ('Air Quality Index URL (IQAIR ONLY) ')
weather = input ('Weather URL (WEATHER.COM CURRENT DAY ONLY) ')
filename = input ('Filename? ')
filename = filename + '.txt'
a = open (filename, 'w+')
a.close()
while True:
    try:
        print ('Writing...')
        f = open(filename + '.txt','a+')
        mystring = '2020:9:11,04:01:02'
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ctime = str(current_time).split (' ')
        currentdate = ctime[0]
        currenttime = ctime[1]
        allow = False
        pm25 = False
        unhealthy = False
        r = requests.get(url)
        rq = requests.get(weather)
        cont = True
        soup = BeautifulSoup(r.text,'html.parser')
        soupq = BeautifulSoup(rq.text, 'html.parser')
        temps = soupq.findAll('div', {'class': '_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK'})
        tempss = re.findall(r'\d+', str(temps)) 
        mydivs = soup.findAll("div", {"class": "aqi-value-wrapper"})

        test = ''
        temp = re.findall(r'\d+', str(mydivs))
        prev = 0
        test = soup.findAll('div', {'class' : 'table-wrapper'})
        allow = True
        if allow == True:
                x = f.read()
                write = str(ctime[0]) + ',' + str(ctime[1]) + ',' + 'PM2.5,'+temp[4]+ ','+ ''+str(tempss[2]) + '\n'
                print (write)
                f.write (str(write))
        time.sleep(300)
    except KeyboardInterrupt:
        sys.exit()
        f.close()
