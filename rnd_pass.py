#!/usr/bin/python

import string, random

def id_generator(size):
	chars = string.letters+string.digits
	return ''.join(random.choice(chars) for _ in range(size))

size = int(raw_input("enter word size: "))
print id_generator(size)
