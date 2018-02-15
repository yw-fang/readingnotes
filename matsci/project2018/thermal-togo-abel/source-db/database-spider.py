import urllib2  # needed for functions,classed for opening urls.

url = raw_input("enter the url needed for downloading file(pdf,mp3,zip...etc)\n");

usock = urllib2.urlopen(url)  # function for opening desired url
file_name = url.split('/')[
    -1]  # Example : for given url "www.cs.berkeley.edu/~vazirani/algorithms/chap6.pdf" file_name will store "chap6.pdf"
f = open(file_name, 'wb')  # opening file for write and that too in binary mode.
file_size = int(usock.info().getheaders("Content-Length")[0])  # getting size in bytes of file(pdf,mp3...)
print
"Downloading: %s Bytes: %s" % (file_name, file_size)

downloaded = 0
block_size = 8192  # bytes to be downloaded in each loop till file pointer does not return eof
while True:
    buff = usock.read(block_size)
    if not buff:  # file pointer reached the eof
        break

downloaded = downloaded + len(buff)
f.write(buff)
download_status = r"%3.2f%%" % (downloaded * 100.00 / file_size)  # Simple mathematics
download_status = download_status + (len(download_status) + 1) * chr(8)
print
download_status, "done"

f.close()