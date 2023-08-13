from webdav4.client import Client
#import sys

client = Client("http://192.168.192.11:6089", auth=("yanlz", "ylz123123"))
print (client.exists("sdb1/download/test"))

print(client.ls("sdb1/download", detail=False))
print(client.upload_file("test.txt", "sdb1/download/test.txt"))