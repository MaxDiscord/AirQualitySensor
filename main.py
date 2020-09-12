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
timedelay = input('Delay (in seconds) between each output to CSV? (leave empty for 300) ')
if timedelay == '':
	timedelay = 300
else:
	timedelay = int(timedelay)
url = "https://www.iqair.com/us/usa/washington/mercer-island?utm_source=homepage_-usa-washington-mercer-island"
weather = 'https://weather.com/weather/today/l/2abe70d2c4e189db21e5a4a82fe9e0e90f4d9c39ba36b4365df44a85caf79fa8'
while True:
	try:
		f = open('belleviewcollege.txt','a+')
		mystring = '2020:9:11,04:01:02'
		current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		ctime = str(current_time).split (' ')
		datee = ctime[0]
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
				print ('Current Date:', datee)
				print ('Current Time:', currenttime)
				print ('Current Air Quality:', temp[4])
				print ('Current Temperature: ', tempss[2])
				print ('\n')
		time.sleep(timedelay)
	except KeyboardInterrupt:
		sys.exit()
		f.close()








	
