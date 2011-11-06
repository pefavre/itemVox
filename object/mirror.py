#!/usr/bin/python

import sys, re, os

def findUriForTag(tag):
	return 'spotify:album:6q3hbicXXa7IyXygYnc1rg'

def openUri(uri):
	cmd = ('./scripts/openAlbum.sh %s ; open ./scripts/play.app' % uri)
	os.system(cmd)


serial=''

while True:
	line = sys.stdin.readline()
	w = re.split('\W+', line)
	if ('SERIAL' == w[0]):
		serial = w[1];
		print "new serial is %s" % (serial)
	elif ('ON' == w[0]):
		tag = w[1];
		print "tag %s is on" % (tag)
		uri = findUriForTag(tag)
		openUri(uri)
	elif ('OFF' == w[0]):
		tag = w[1];
		print "tag %s is off" % (tag)
