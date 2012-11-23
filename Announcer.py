# -*- coding: utf-8 -*-
from MayhemCookiesHandler import MayhemCookiesHandler
from MayhemRequestHandler import MayhemRequestHandler
import time as xtime
from time import localtime, strftime
import sys
import re

class Announcer:
	def __init__(self, interval):
		self.interval = interval
		self.message = ''
		self.verbosity = 1
		self.payload = None

	def prepare(self, m):
		self.message = m
		page = MayhemCookiesHandler(1)
		self.payload = MayhemRequestHandler("http://www.modelmayhem.com/announce/save", page, self.verbosity)
		
		return self
	
	def send(self):
		
		while True:
			try:
				t = self.payload.launchAnnounceRequest(self.message)
				self.decodeResponse(t)
				xtime.sleep(self.interval)
			except KeyboardInterrupt:
				print "Exiting gracefully..."
				sys.exit()
		
		return self
		
	def decodeResponse(self, response):
		exectime = strftime("%Y-%m-%d %H:%M:%S", localtime())
		if re.findall ('You must wait', response) != None:
			print exectime, "Timeout not yet reached."
		elif re.findall ('Make an', response) != None:
			print exectime, "Message announced."
		else:
			print exectime, "Unknown response."
		
		return 0