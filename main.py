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

#url = "https://www.iqair.com/us/usa/washington/bellevue/bellevue-college"
#weather = 'https://weather.com/weather/today/l/b12dbcb51efb956165d715e15d87a6cba9b8fcc4a06d820f9c7e8778422c10f6'
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
        if 'PM2.5' in str(test):
                #print ('Primary Pollutant: PM2.5')
                pm25 = True

                unhealthy = True

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
