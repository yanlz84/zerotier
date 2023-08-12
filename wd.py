from webdav import WebDAVClient
# 连接到WebDAV服务器
def upload(url,un,pw,fp)
client = WebDAVClient(
    url,  # WebDAV服务器URL
    username=un,  # 用户名
    password=pw   # 密码
)
# 指定要上传的文件和目标路径
file_path = fp  # 要上传的文件路径
remote_path = "/Download"  # 目标路径
# 上传文件
client.upload(file_path, remote_path)
upload(url,un,pw,fp)
