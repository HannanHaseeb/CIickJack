#!/usr/bin/python2

from sys import argv
import time 
import os
import urllib2
import requests

print ("[+]Checking ClickJacking on each subdomain in list")
script, filename = argv
f = open(filename, "r+");
subdomains = f.readline();
count = 0;
for subdomain in subdomains: 
    newsubdomain = "http://%s" % subdomain
    try:
      a = urllib2.urlopen(newsubdomain)
      code=a.getcode();
      if a.info().getheader('X-Frame-Options')!="SAMEORIGIN" and a.info().getheader('X-Frame-Options')!="DENY":
         print "\r Domain : %s is Vulernable To ClickJacking!" % (newsubdomain)
      else:
         print "\r Domain : %s Not Vulernable To Click Jacking" % (newsubdomain)

    except urllib2.HTTPError, e:
           code = e.code
           print "\r Domain : %s Not Vulernable To Click Jacking" % (newsubdomain)
    except urllib2.URLError, e:
           print "\r Domain : %s Not Vulernable To Click Jacking" % (newsubdomain)
