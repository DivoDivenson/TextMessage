#!/usr/bin/env python
import sys, re

word_list = {}

if __name__ == "__main__":
	if sys.argv[1] == "-":
		for line in sys.stdin.readlines():
			parts = re.split("\W+", line)
			for i in parts:
				try:
					word_list[i] = word_list[i] + 1
				except KeyError:
					word_list[i] = 1
	for k,v in word_list.iteritems():
		print k + ":\t" + str(v)
	#Take it from here div
				
