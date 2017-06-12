#graph

import serial
import matplotlib.pyplot as plt
import time
from time import sleep

ser = serial.Serial('/dev/ttyACM0')

plt.ion()

df = list()
dat = list()
c = 0
x = list()

while 1:
	dat = ser.readline().decode().strip()
	dat = float(dat)
	df.append(dat)

	c+=1

	#print(df)

	x.append(c)

	plt.plot(x, df, 'ro--')
	plt.pause(0.1)
	plt.show()
	sleep(1)

