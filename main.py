#!/usr/bin/env python

import os
import pdb
from nyc import getCor

def addZero (x):
	retStr= str(x)
	if (x< 10):
		retStr = "0" + retStr
	return retStr
	
def mkmapsForDay(dirName, day):
	i = 0
	for h in range(0,24):
		for m in range(0,6):
			fname = dirName + str(i)+".html"
			if (i == 0):
				fname = dirName + "index.html"
			print fname
			c = "2013-07-"+addZero(day) + " " + addZero(h) + ":"+str(m)
			print (c)
			i+=1
			thisUrlText = "2013-07-"+addZero(day) + " " + addZero(h) + ":"+addZero((m)*10)
			print thisUrlText
			nextUrl = "http://akuchlous.github.io/NYC_CAB_ANALYTICS/July/1/"+str(i) +".html"
			nextUrlText = "2013-07-"+addZero(day) + " " + addZero(h) + ":"+addZero((m+1)*10)
			print nextUrlText
			if (m == 5):
				nextUrlText = "2013-07-"+addZero(day) + " " + addZero(h+1) + ":"+addZero(0)
			if (h == 23 and m == 5) :
				nextUrl  = "http://akuchlous.github.io/NYC_CAB_ANALYTICS/"
				nextUrlText = "new day"
			print 
			print 
			getCor(c,  fname, thisUrlText, nextUrl, nextUrlText)

def getMapsForDay(day, month):
	fname = month + "/"+ str(day) + "/"
	if (os.path.exists(fname) == False):
		os.mkdir(fname)
	mkmapsForDay(fname, day)

def main():
	for x in range(1,31):
		getMapsForDay(x, "July")

if __name__ == "__main__":
	main()
