from webdav4.client import Client
import sys

client = Client(sys.argv[1], auth=("sys.argv[2]", "sys.argv[3]"))
#print (client.exists("sdb1/download/test"))

#print(client.ls("sdb1/download", detail=False))
client.upload_file("test.txt", "sdb1/download/test.txt")