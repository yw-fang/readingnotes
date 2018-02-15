import urllib2
import re
import urllib

#define url
url='http://phonondb.mtl.kyoto-u.ac.jp/raw_data/'
website = urllib2.urlopen(url)
#read html code
html = website.read()
#use re.findall to get all the links
links = re.findall('"((http)s?://.*.tar.lzma)"', html)

pattern = re.compile(r'mp-\d+.tar.lzma')  #here, mp-\d+.tar.lzma is the pattern
matchlist = pattern.findall(html)  #note in this matchlist, the comound ID is printed twice.
new_matchlist = matchlist[::2]
print(new_matchlist[:10])
print(type(new_matchlist))
#print(' '.join(matchlist))  #through joinining, the quotations are removed. 

for i in new_matchlist:
    file_url = 'http://phonondb.mtl.kyoto-u.ac.jp/raw_data/' + str(i)
    print(file_url)

#urllib.urlretrieve(url, 'mp-25.tar.lzma')
