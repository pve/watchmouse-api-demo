#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# DEMO program, to get performance report from Watchmouse / CA Cloud monitor

import urllib2, json
import os

from time import gmtime, strftime
today = strftime("%Y-%m-%d", gmtime())

nkey = os.getenv('WMNKEY', 'novalidkey' )
# the command environment will hold the Authentication NKEY

mytags = "&tags=myproduction"

startdate = "&start_date=" + today

url = "https://api.cloudmonitor.ca.com/1.6/rule_stats?nkey=" + nkey + mytags + startdate + "&callback=json"

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

print str(totalerrors + " / " + totalchecks)



