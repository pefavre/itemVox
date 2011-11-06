#!/bin/sh

cd $(dirname $0)

./buttons.py /dev/tty.usb*
