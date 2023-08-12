import easywebdav
import sys
webdav = easywebdav.connect(sys.argv[1],port=6089, username=sys.argv[2], password=sys.argv[3])
webdav.upload('test', '/sdb1/download/test')
#print (webdav.ls())
