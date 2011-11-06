#!/bin/sh

cd $(dirname $0)

./mirror_read/mirror_read | ./mirror.py
