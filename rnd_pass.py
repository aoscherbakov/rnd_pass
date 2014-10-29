#!/usr/bin/python

import string, random

def id_generator(size):
	chars = string.letters+string.digits
	return ''.join(random.choice(chars) for _ in range(size))

size = 8

while 1:
	#size = int(raw_input("enter pass size: "))
	print id_generator(size)
	raw_input("Press Enter")
