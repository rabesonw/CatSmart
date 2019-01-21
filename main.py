from moves import Moves 
from relay import Relay 
from camera import Camera 
from scale import Scale 

import os
import time

class CatSmart(object):

	def __init__(self):
		self.mov = Moves()
		self.rel = Relay()
		self.cam = Camera()
		self.sca = Scale()

	def main(self):
		while True:
			weight = self.sca.weigh()
			if weight < 10 and self.mov.detect() == False:
				self.rel.on()
				time.sleep(8)
				self.rel.off()
			if self.mov.detect():
				self.cam.stream()
				os.system('vlc rtsp://ig-rasp45:8554/ &')
				time.sleep(60)
				self.cam.stop()
		
cat = CatSmart()
cat.main()