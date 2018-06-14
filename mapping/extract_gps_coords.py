import sys, os
import pynmea2
import math

for line in open(sys.argv[1]):
	nmea_line = line.split('/')[1]
	nmea_line_split = nmea_line.split(',')

	lat_pseudo = float(nmea_line_split[2])/100.0
	lat_int = math.floor(lat_pseudo)
	lat_frac = (lat_pseudo-lat_int)*100.0/60.0
	lat = lat_int + lat_frac
	
	lon_pseudo = float(nmea_line_split[4])/100.0
	lon_int = math.floor(lon_pseudo)
	lon_frac = (lon_pseudo-lon_int)*100.0/60.0
	lon = lon_int + lon_frac


	lat = str(lat) + " " + nmea_line_split[3]
	lon = str(lon) + " " + nmea_line_split[5]
	print 'foo, ' + 'bar, ' + lat, ',', lon
