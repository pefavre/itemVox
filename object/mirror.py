#!/usr/bin/python

import sys, re, os

associations = {
	'0008d00218bd6e5669d7' : 'spotify:album:3Y8O9H5qRkyqYEgwNhzwUW' # autumn falling
	, '0008d00218c10916b3a3' : 'spotify:album:5iQkt7Mx6B0oWTMhZoKHYC' # back to the future
	, '0008d00218c10916c6df' : 'spotify:album:0nMpXqkS4Attun6WWrHGvv' # hot club du france 1947
	, '0008d00218bd6e566cc8' : 'spotify:album:73atzd4xK9PMS4iGanT9un' # joplin
	, '0008d00218bd6e566d08' : 'spotify:album:7exqkn1MEoUhfDRMjwCOgm' # fucked up
	, '0008d00218bd6e566ead' : 'spotify:album:0PTD76vhQLnOSdmTfH3qg1' # asian dub
	, '0008d0021a0353184589' : 'spotify:album:4McrRTxFA51hl3Gy8Er2da' # lapin bleu
	, '0008d00218bd6e566eed' : 'spotify:album:1zRIx14J26U6SANgfShypH' # lanterns on the lake
	, '0008d00218c10916bdc0' : 'spotify:album:0CgTKS2HmWc3JeI9Fit2vX' # barbershop / sweeney todd
	, '0008d00218bd6e566997' : 'spotify:album:32ZaJ7p8xvsYE8udh6vyOg' # joe dassin
}


def findUriForTag(tag):
	uri = associations[tag]
	return uri

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
