import easywebdav
webdav = easywebdav.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])
webdav.upload('test', '/Download/test')
