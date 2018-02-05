import urllib3
import re
  
url = 'http://phonondb.mtl.kyoto-u.ac.jp/raw_data/'
  
req = urllib3.Request(url)
con = urllib3.urlopen(req)
doc = con.read()
con.close()
  
#links = re.findall(r'href\=\"(http\:\/\/[a-zA-Z0-9\.\/]+)\"', doc)
links = re.findall(r'href\=\"(http\:\/\/[phonondb\.\/]+)\"', doc)
for a in links:
  print(a)
