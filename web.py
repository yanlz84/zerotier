from webdav4.client import Client
import sys
import requests
import os

print(sys.argv[0:])
r=requests.get(sys.argv[4])
if r.status_code == 200:
    file_name = os.path.basename(sys.argv[4]) 
    with open(file_name, 'wb') as f:  # 打开文件，以二进制写入模式
        f.write(r.content)
client = Client(sys.argv[1], auth=(sys.argv[2], sys.argv[3]))
#print (client.exists("sdb1/download/test"))

#print(client.ls("", detail=False))
print(client.upload_file(file_name, "sdb1/download/"+file_name))