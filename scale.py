import RPi.GPIO as gpio 
import threading
import time

class Scale(object):

	def __init__(self):
		self.DAT=13
		self.CLK=7
		gpio.setwarnings(False)
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.CLK, gpio.OUT)

	def weigh(self):
		i = 0
		num = 0
		gpio.setup(self.DAT, gpio.OUT)
		gpio.output(self.DAT, 1)
		gpio.output(self.CLK, 0)
		gpio.setup(self.DAT, gpio.IN)

		while gpio.input(self.DAT) == 1:
			i = 0
		for i in range(24):
			gpio.output(self.CLK, 1)
			num = num<<1

			gpio.output(self.CLK, 0)

			if gpio.input(self.DAT) == 0:
				num = num + 1

		gpio.output(self.CLK, 1)
		num = num ^0x800000
		gpio.output(self.CLK, 0)
		wei = 0
		wei = ((num)/1406)
		return (wei-6020)-95
		time.sleep(0.5)