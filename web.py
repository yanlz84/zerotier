from webdav4.client import Client
import sys
import requests

#print(sys.argv[0:])
r=requests.get(sys.argv[4],allow_redirects=True)
if r.status_code == 200:
    content_disposition = r.headers.get('Content-Disposition')
    if content_disposition:
        filename = content_disposition.split('=')[1].replace('"', '')
    else:
        filename = sys.argv[4].split('/')[-1]
with open(filename, 'wb') as f:
    f.write(r.content)

print(filename)
#client = Client(sys.argv[1], auth=(sys.argv[2], sys.argv[3]),verify=False)
#print (client.exists("sdb1/download/test"))
client = Client(sys.argv[1], auth=(sys.argv[2], sys.argv[3]))
print('upload file')

#print(client.ls("", detail=False))
print(client.upload_file(filename, "sdb1/video/download/"+filename))
