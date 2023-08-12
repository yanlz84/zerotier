import easywebdav
# 连接到WebDAV服务器
client = WebDAVClient(
    sys.argv[1],  # WebDAV服务器URL
    username=sys.argv[2],  # 用户名
    password=sys.argv[3]   # 密码
)
# 指定要上传的文件和目标路径
#file_path = sys.argv[4]  # 要上传的文件路径
#remote_path = "/Download"  # 目标路径
# 上传文件
client.upload(file_path, remote_path)

webdav = easywebdav.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
webdav.upload('test', '/Download/test')
