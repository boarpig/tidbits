#!/usr/bin/python2
#eccoding: utf8

from BeautifulSoup import BeautifulSoup
import urllib

f = urllib.urlopen("http://weather.willab.fi/weather.html.fi")
soup = BeautifulSoup(f.read())
tulos = soup.find("p", "tempnow")

print(tulos.contents[0].replace(u"&deg;", u"°"))
