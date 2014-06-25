#!/usr/bin/env python

import sys 
import pdb

filename = "trip_data_7.csv"
fHandle = None

def openFile(fn):
	def wrapped():
		global filename, fHandle
		fHandle = open(filename, "r")
		fn()
		fHandle.close()
	return wrapped

@openFile
def passengersPerTrip():
	global fHandle
	dist = {}
	i=0
	for line in fHandle:
		if (i == 0):
			i+=1
			continue
		i+=1
		d = line.split(",")[7]
		dF = float(d)
		dInt = int(dF)
		if (dInt not in dist):
			dist[dInt] = 0
		dist[dInt] +=1
	print ("Passenger Distribution")
	print "Total Trips: %d" %i
	for d in dist:
		print ("%d,%d" %(d, dist[d]))

@openFile
def milesPerTrip():
	global fHandle
	dist = {}
	i=0
	for line in fHandle:
		if (i == 0):
			i+=1
			continue
		i+=1
		d = line.split(",")[9]
		dF = float(d)
		dInt = int(dF)
		if (dInt >100):
			dInt = 100
		if (dInt not in dist):
			dist[dInt] = 0
		dist[dInt] +=1
	print ("Trip Distance ")
	print "Total Trips: %d" %i
	for d in dist:
		print ("%d,%d" %(d, dist[d]))


@openFile
def getLicPerMed():
	global fHandle
	m2l = {}		#medallion to license
	l2m = {}		#license to medallion
	i = 0
	for line in fHandle:
		if (i == 0):
			i+=1
			continue
		i+=1
		spl = line.split(",")
		m = spl[0] #medallion
		l = spl[1] #license
		if (m not in m2l):
			m2l[m] = []
		if (l not in m2l[m]):
			m2l[m].append(l)

		if (l not in l2m):
			l2m[l] = []
		if (m not in l2m[l]):
			l2m[l].append(m)

	# avg lic per medallion / tax 
	print "Total Medallions: %s"% len(m2l)
	print "Total Licenses: %s"% len(l2m)

	# avg drivers operating a single taxi  : uniq ppl that get to drive 1 tax 
	dist = {}
	total = 0
	for m in m2l:
		l = len(m2l[m])
		total += l
		if (l not in dist):
			dist[l] = 0
		dist[l] +=1

	print "Avg Number Of Different Drivers Per Taxi : %d"% (total/len(m2l))
	for d in dist:
		print ("Taxi's with %d uniq drivers : %d"%(d, dist[d]))
	
	# avg taxi per single driver  : uniq taxi that get driven by driver
	taxi = {}
	total = 0
	for l in l2m:
		t = len(l2m[l])
		total += t
		if (t not in taxi):
			taxi[t] = 0 
		taxi[t]+=1

	print "Avg Number Of Differnet Taxi Per Driver : %d"% (total/len(l2m))
	for t in taxi:
		print ("Drivers's with %d different taxi: %d" %(t, taxi[t]))

def main():
	# getLicPerMed()
	# milesPerTrip()
	# passengersPerTrip()
	# tripsPerCarPerDay()
	# tripsByDayOfMonth()
	# tripsByDayOfWeek()
	# tripsByHourOfDay()
	# avgTimePerTrip()
	# avgTimePerTripByHour()


if __name__ == "__main__":
	main()
