###########################################
# Simple Makefile for HIDAPI test program
#
# Alan Ott
# Signal 11 Software
# 2010-07-03
###########################################

TARGET=mirror_read

all: ${TARGET}

CC=gcc
CXX=g++
COBJS=hid.o
CPPOBJS=main.o
OBJS=$(COBJS) $(CPPOBJS)
CFLAGS+= -Wall -g -c 
LIBS=-framework IOKit -framework CoreFoundation


${TARGET}: $(OBJS)
	g++ -Wall -g $^ $(LIBS) -o ${TARGET}

$(COBJS): %.o: %.c
	$(CC) $(CFLAGS) $< -o $@

$(CPPOBJS): %.o: %.cpp
	$(CXX) $(CFLAGS) $< -o $@

clean:
	rm -f *.o ${TARGET} $(CPPOBJS)

.PHONY: clean
