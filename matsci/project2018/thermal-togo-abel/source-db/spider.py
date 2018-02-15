import urllib2
import re
from tempfile import TemporaryFile

#define url
url='http://phonondb.mtl.kyoto-u.ac.jp/raw_data/'
website = urllib2.urlopen(url)
#read html code
html = website.read()
#use re.findall to get all the links
links = re.findall('"((http)s?://.*.tar.lzma)"', html)
#print(html)

pattern = re.compile(r'mp-\d+.tar.lzma')  #here, mp-\d+.tar.lzma is the pattern
findpattern = pattern.findall(html)
print(type(findpattern))
print(' '.join(findpattern))
