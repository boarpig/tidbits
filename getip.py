#!/usr/bin/python

import re
from urllib.request import urlopen
try:
    haku = re.compile("your ip address is (?P<osoite>(\d{1,3}\.){3}\d{1,3}) ", re.I)
    page = urlopen("http://www.checkmyip.org/")
    content = page.read()
    result = haku.search(str(content))
    print(result.group('osoite'))
except AttributeError:
    print("couldn't retrieve ip")
except IOError:
    print("couldn't find ip-server")
finally:
    page.close()

