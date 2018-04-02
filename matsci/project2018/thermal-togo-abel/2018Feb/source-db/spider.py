#Author: Yue-Wen FANG at Kyoto University
#Contact: fyuewen@gmail.com
######################################################
#Purpose: This is a python crawler/spider to download#
#the phonon database maintained by Togo-sensei       #
#python 2.x should be used.
#usage: python spider.py
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
new_matchlist = matchlist[::2] #Here, I selected all the matched iterms, and discarded the duplicated ones
print(new_matchlist[:10])
print(type(new_matchlist))
#print(' '.join(matchlist))  #through joinining, the quotations are removed. 

for i in new_matchlist:
    file_url = 'http://phonondb.mtl.kyoto-u.ac.jp/raw_data/' + str(i)
    urllib.urlretrieve(file_url, i) #download files with the name of i.
    print(file_url)
#usage of urllib.urlretrieve
#urllib.urlretrieve(url, filename) #here, filename should be a string
