import urllib


host = 'http://phonondb.mtl.kyoto-u.ac.jp/raw_data/'

url = 'http://phonondb.mtl.kyoto-u.ac.jp/raw_data/'+'mp-25.tar.lzma'

urllib.urlretrieve(url, 'mp-25.tar.lzma')
