from picamera import PiCamera 
import os
from time import sleep
from subprocess import check_output


class Camera(object):
	
	def __init__(self):
		self.camera = PiCamera()

	def film(self):
		self.camera.start_preview()
		self.camera.start_recording('/home/pi/vid.h264')
		time.sleep(10) #inefficient for long recordings
		self.camera.wait_recording(10) #better for longer recordings
		self.camera.stop_recording()
		self.camera.stop_preview()
		#https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

	def getPid(name):
		return map(int, check_output(["pidof", name]).split())

	def stream():
		os.system("./stream.sh")

	def stop():
		pids = getPid("vlc")
		for pid in pids:
			os.system("kill "+ str(pid))