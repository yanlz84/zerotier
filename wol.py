import sys
import paramiko

# 创建SSH客户端
client = paramiko.SSHClient()
# 自动添加服务器的SSH密钥（这将跳过服务器密钥验证，请确保你知道这样做的风险）
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
your_ssh_server_ip=sys.argv[0:]
your_username=sys.argv[1:]
your_password=sys.argv[2:]
your_command=sys.argv[3:]


# 连接到SSH服务器
client.connect(your_ssh_server_ip, username=your_username, password=your_password, port=2233)

# 在SSH服务器上执行命令
stdin, stdout, stderr = client.exec_command(your_command)

# 打印命令输出
print(stdout.read().decode('utf-8'))

# 关闭连接
client.close()
