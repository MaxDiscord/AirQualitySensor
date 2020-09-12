from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import datetime
import time
import sys
pm25=True
timedelay = input('Delay (in seconds) between each output to CSV? (leave empty for 300) ')
if timedelay == '':
	timedelay = 300
else:
	timedelay = int(timedelay)
url = input ('IQAIR Link ')
weather = input ('Weather.com Link ')
while True:
	try:
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
		test = soup.findAll('div', {'class' : 'table-wrapper'})
		print ('Current Date:', datee)
		print ('Current Time:', currenttime)
		print ('Current Air Quality:', temp[4])
		print ('Current Temperature: ', tempss[2])
		print ('\n')
		time.sleep(timedelay)
	except KeyboardInterrupt:
		sys.exit()
		f.close()








	
