#!/usr/bin/env python

import sys
import pdb
from datetime import datetime

head = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Heatmaps</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
      #panel {
        position: absolute;
        top: 5px;
        left: 20%;
        margin-left: -180px;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=visualization"></script>
    <script>
// Adding 500 Data Points
var map, pointarray, heatmap;

var taxiData = [
'''

end0 = '''
];
function initialize() {
  var mapOptions = {
    zoom: 12,
    center: new google.maps.LatLng(40.76284 , -73.905),
    mapTypeId: google.maps.MapTypeId.MAP
  };
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  var pointArray = new google.maps.MVCArray(taxiData);
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: pointArray
  });
  heatmap.setMap(map);
}


google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>

  <body>
    <div id="panel">
Guide For Uber Drivers Where Passengers are: <a href="http://chriswhong.com/open-data/foil_nyc_taxi/">Based on taxi data </a></br>
<b>
'''

end1 = '''
</b>
</br> 
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- mapadsmall -->
<ins class="adsbygoogle"
     style="display:inline-block;width:320px;height:50px"
     data-ad-client="ca-pub-2853949053079340"
     data-ad-slot="4253984965"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
<a href="http://twikstik.com/"> Brought to you by :twikstik.com :  Bay Area Real Estate</a></br> 
'''

end2 = '''
    </div>
    <div id="map-canvas"></div>
  </body>
</html>
'''

week   = [
        'Monday', 
        'Tuesday', 
        'Wednesday', 
        'Thursday',  
        'Friday', 
        'Saturday'
	'Sunday', 
	]


data = {}

def readDict():
	global data 
	f = open ("trip_data_7.csv", "r")
	i = 0
	for line in f :
		if (i == 0):
			i+=1
			continue
	 	tokens = line.split(",")
		data[tokens[5]] = (tokens[11], tokens[12])
	f.close()


def getCor(t, fname, tUrlTxt = None, nUrl=None, nUrlText=None):
	# pdb.set_trace()
	global data
	if (data == {}):
		readDict()
	mainF = open(fname, "w")
	mainF.write(head)
	# t = sys.argv[1]
	day,hr = t.split(" ")
	s = datetime.strptime(day, '%Y-%m-%d')   #Jun 7 200
	w = s.weekday()
	i = 0 
	buf= ""
	for key in data:
		if (i > 2500):
		   	break
	 	if (t in key):
			i+=1
			a,b = data[key]
			if (a == "0"  or a == ""  or b =="0" or b ==""):
				continue
  			# buf += "new google.maps.LatLng("+tokens[11]+","+tokens[12]+"),\n"
  			buf = "new google.maps.LatLng("+a+","+b+"),\n"
  			# buf += "F("+tokens[11]+","+tokens[12]+"),"
	 		mainF.write(buf)
	print i
	mainF.write(end0)	
	# pdb.set_trace()
	# if (":" in hr):
	# 	hr = hr.split(":")[0]
	# hrI = int(hr)
	# am_pm = " AM" 
	# if (hrI >= 12) : 
	# 	am_pm =  "PM"
	# 	if (hrI > 12) : 
	# 		hrI = hrI-12
	# buf = day + " " +str(hrI)+"0" + am_pm +" : " + " " + week[s.weekday()]
	mainF.write( tUrlTxt + week[s.weekday()])
	# time =  day + " " + hr + am_pm +" : " + " " + week[s.weekday()]
	mainF.write(end1)
	if (nUrl):
		mainF.write(' <i> Next <a href="' + nUrl + '">' + nUrlText + '</a></i>')
	mainF.write(end2)
	mainF.close()
	# return (time, buf)


def main():
	getCor("2013-07-01 01:0", "data.html")

if __name__ == "__main__":
	main()
