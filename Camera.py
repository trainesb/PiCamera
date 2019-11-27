########################################################################
#
# Author: Ben Traines
# Date: 11/22/2019
# Description: 
#
########################################################################

import io
import cv2
import PIL
import time
import numpy as np
from picamera import PiCamera
from fraction import Fraction

class Camera():
	
	
	def __init__(slef):
		self.camera = PiCamera()
		self.width = 1024
		self.height = 768
		self.zoom = 50
		self.led = True
		
		
		#self.camera.framerate = 10
		#self.rawCapture = PiRGBArray(self.camera, size=(self.CAM_WIDTH, self.CAM_HEIGHT))
		#self.rawCapture.truncate(0)
		
	def set_resolution(self, width, height):
		"""Sets the camera resolution."""
		self.camera.resolution = (int(width), int(height))
		
	def set_width(self, n):
		"""Sets the image width."""
		self.width = int(n)
		
	def set_height(self, n):
		"""Set the image height."""
		self.cam_height = n
		
	def capture_to_file(self, fileName):
		"""Capture image to a file."""
		self.set_resolution(self.cam_width, self.cam_height)
		self.camera.start_preview()
		time.sleep(2)
		self.camera.capture(fileName+'.jpg')
			
	def capture_to_stream(self, fileName):
		"""Capture image to a stream."""
		my_file = open(fileName+'.jpg', 'wb')
		self.camera.start_preview()
		time.sleep(2)
		self.camera.capture(my_file)
		my_file.close()
			
	def capture_to_PIL(self):
		"""Capture image to a PIL."""
		self.stream = BytesIO()
		self.camera.start_preview()
		time.sleep(2)
		self.camera.capture(self.stream, format='jpeg')
		# "Rewind" the stream to the beginning
		stream.seek(0)
		return Image.open(self.stream)
		
	def resize(self, fileName):
		"""Resize an image."""
		self.camera.resolution = (self.width, self.height)
		self.camera.start_preview()
		time.sleep(2)
		self.camera.capture(fileName+'.jpg', resize=(self.width, self.height))
		
	def capture_consistent(self):
		self.camera.resolution = (1280, 720)
		self.camera.framerate = 30
		self.camera.iso = 100
		time.sleep(2)
		self.camera.shutter_speed = self.camera.exposure_speed
		self.camera.exposure_mode = 'off'
		g = self.camera.awb_gains
		self.camera.awb_mode = 'off'
		self.camera.awb_gains = g
		self.camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
		
	def capture_timelapse(self, time):
		self.camera.start_preview()
		time.sleep(2)
		for filename in self.camera.capture_contnuous('img{counter:03d}.jpg'):
			print('Captured %s' % filename)
			time.sleep(time)
			
	def low_light_mode(self, filename):
		self.camera.resolution = (1280, 720)
		self.camera.framerate = Fraction(1, 6)
		self.camera.sensor_mode = 3
		self.camera.shutter_speed = 6000000
		self.camera.iso = 800
		time.sleep(30)
		self.camera.exposure_mode = 'off'
		self.camera.capture(filename + '.jpg')
		
	def record_video(self, filename, time):
		self.camera.resolution = (640, 480)
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
	
