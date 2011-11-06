#!/usr/bin/python

import os, sys
import serial

if (len(sys.argv) < 2):
	print "need /dev/tty.usb* arg"
	quit()

ttyArduino = sys.argv[1]

se = serial.Serial(ttyArduino, 9600)

serial=''

while True:
	line = se.readline();
	line = (line.splitlines())[0];
	line.strip()
	print 'line read : %s' % (line)
	if ('playpause' == line):
		os.system('./scripts/playpause.sh')
	elif ('prev' == line):
		os.system('./scripts/prev.sh')
	elif ('next' == line):
		os.system('./scripts/next.sh')
	elif ('vminus' == line):
		os.system('./scripts/volDown.sh')
	elif ('vplus' == line):
		os.system('./scripts/volUp.sh')
