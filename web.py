from webdav4.client import Client
import sys
print(sys.argv[0:])
client = Client(sys.argv[1], auth=(sys.argv[2], sys.argv[3]))
#print (client.exists("sdb1/download/test"))

#print(client.ls("sdb1/download", detail=False))
print(client.upload_file("test.txt", "sdb1/download/test.txt"))