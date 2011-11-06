/*******************************************************
 Windows HID simplification

 Alan Ott
 Signal 11 Software

 8/22/2009

 Copyright 2009, All Rights Reserved.
 
 This contents of this file may be used by anyone
 for any reason without any conditions and may be
 used as a starting point for your own applications
 which use HIDAPI.
********************************************************/

#include <stdio.h>
#include <wchar.h>
#include <string.h>
#include <stdlib.h>
#include "hidapi.h"

#include <unistd.h>

int main(int argc, char* argv[])
{
	int res;
	unsigned char buf[256];
	#define MAX_STR 255
	wchar_t wstr[MAX_STR];
	hid_device *handle;

	// Open the device using the VID, PID,
	// and optionally the Serial number.
	////handle = hid_open(0x4d8, 0x3f, L"12345");
	handle = hid_open(0x1da8, 0x1301, NULL);
	if (!handle) {
		printf("unable to open device\n");
 		return 1;
	}

	// Read the Serial Number String
	wstr[0] = 0x0000;
	res = hid_get_serial_number_string(handle, wstr, MAX_STR);
	if (res < 0)
		printf("Unable to read serial number string\n");
	printf("SERIAL %ls", wstr);
	printf("\n");


	// Read requested state. hid_read() has been set to be
	// non-blocking by the call to hid_set_nonblocking() above.
	// This loop demonstrates the non-blocking nature of hid_read().
	while (1) {
		res = 0;
		while (res == 0) {
			res = hid_read(handle, buf, sizeof(buf));
			if (res == 0) {
				// printf("waiting...\n");
				;
			}
			else if (res < 0) {
				fprintf(stderr, "Unable to read()\n");
				break ;
				;
			}
			else {
				if (buf[0] == 0x02) // mir:ror report
				{
					switch (buf[1]) {
						case 1: { // tag ON
							printf("ON %02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx\n", 
							buf[3], buf[4], buf[5], buf[6], buf[7], buf[8], buf[9], buf[10], buf[11], buf[12]);
							break ;
						}
						case 2: { // tag OFF
							printf("OFF %02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx%02hhx\n", 
							buf[3], buf[4], buf[5], buf[6], buf[7], buf[8], buf[9], buf[10], buf[11], buf[12]);
							break ;
						}
						default: printf("ERR\n"); break ;
					}
				}
			}
			usleep(1000);
		}
	}

	hid_close(handle);

	/* Free static HIDAPI objects. */
	hid_exit();

	return 0;
}
