#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# DEMO program, to get performance report from Watchmouse / CA Cloud monitor

import urllib2, json
import os

nkey = os.getenv('WMNKEY', 'novalidkey' )
# the command environment will hold the Authentication NKEY
#startdate = today()


url = "https://api.cloudmonitor.ca.com/1.6/rule_stats?nkey=" + nkey + "&tags=myproduction&start_date=2013-09-22&callback=json"

try:
  jsonp = urllib2.urlopen(url).read()
# there does not seem to be a way to get raw JSON out of watchmouse. 
  jsondata = jsonp[ jsonp.index("(")+1 : jsonp.rindex(")") ]
  data = json.loads(jsondata)
  print json.dumps(jsondata, indent=4, separators=(',',':'))
  print data

except urllib2.URLError, e:
  print 'no valid data received' 

print "\n here are the results"

#with data['result']['stats'][0] as res:
totalchecks = data['result']['stats'][0]['checks'] 
totalerrors = data['result']['stats'][0]['check_errors']

bad = " "
# f totalerrors > (0.05 * totalchecks)i: bad = " BAD"

print totalerrors + " / " + totalchecks + bad



