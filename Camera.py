########################################################################
#
# Author: Ben Traines
# Date: 11/22/2019
# Description: 
#
########################################################################

from io import BytesIO

import time
from time import sleep

import numpy as np
import cv2

import picamera
from picamera import PiCamera
from PIL import Image

class Camera():
	
	self.CAM_WIDTH = 1024
	self.CAM_HEIGHT = 768
	self.ZOOM = 50
	self.LED = True
	
	def __init__(slef):
		self.camera = PiCamera()
		self.camera.resolution = (self.CAM_WIDTH, self.CAM_HEIGHT)
		self.camera.start_preview()
		# Camera warm-up time
		sleep(2)
		
		
		self.camera.framerate = 10
		self.rawCapture = PiRGBArray(self.camera, size=(self.CAM_WIDTH, self.CAM_HEIGHT))
		self.rawCapture.truncate(0)
		
	def screen_shot(self, fileName):
		try:
			self.camera.capture(fileName + '.jpg')
			return True
		except:
			return False
			
	def capture_stream(self):
		try:
			# Create in-memory stream
			stream = BytesIO()
			self.camera.capture(stream, 'jpeg')
			return stream
		except:
			return False
			
	def capture_to_PIL(self):
		stream = self.capture_stream()
		# "Rewind" the stream to the beginning
		stream.seek(0)
		return Image.open(stream)
		
	def capture_size(self, file, width, height):
		self.camera.capture(file+'.jpg', resize=(width, height))
		
	def capture_timelapse(self, time):
		for filename in self.camera.capture_contnuous('img{counter:03d}.jpg'):
			print('Captured %s' % filename)
			sleep(time)
			
	def low_light_mode(self, filename):
		self.camera.framerate = Fraction(1, 6)
		self.camera.sensor_mode = 3
		self.camera.shutter_speed = 6000000
		self.camera.iso = 800
		sleep(30)
		self.camera.exposure_mode = 'off'
		self.camera.capture(filename + '.jpg')
		
	def record_video(self, fileName, time):
		self.camera.start_recording(filename+'.h264')
		self.camera.wait_recording(time)
		self.camera.stop_recording()
		
	def LED_switch(self):
		if self.LED:
			self.LED = False
		else:
			self.LED = True
		self.camera.led = self.LED
		
	def capture_to_numpy_ary(self):
		with self.camera as camera:
			camera.resolution = (320, 240)
			camera.framerate = 24
			time.sleep(2)
			output = np.empty(240, 320, 3)), dtype=np.unit8)
			camera.capture(output, 'rgb')
			
	def capture_to_OpenCV(self):
		with self.camera as camera:
			camera.resolution(320, 240)
			camera.framerate = 24
			time.sleep(2)
			image = np.empty((240 * 320 * 3,), dtype=np.unit8)
			camera.capture(image, 'bgr')
			image = image.reshape((240, 320, 3))
			return image
		
	def zoom(self, n):
		camera.zoom((n/100., n/100., 0.5, 0.5)
		self.zoom = n
		return self.zoom
	
